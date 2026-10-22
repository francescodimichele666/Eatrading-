"""Prove del bot con un finto MT5: python -m unittest discover tests"""

import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from finto_mt5 import TIPO_BARRE, mt5, stato  # noqa: E402

sys.modules["MetaTrader5"] = mt5

from bot import principale  # noqa: E402
from bot.orari import NEW_YORK, ORE_BROKER_SU_NEW_YORK  # noqa: E402
from bot.strategia_b import atr_wilder, decidi  # noqa: E402
from bot import strategia_rumore  # noqa: E402


def secondi_broker(ora_ny: datetime) -> int:
    return int((ora_ny.replace(tzinfo=None) + timedelta(hours=ORE_BROKER_SU_NEW_YORK)
                - datetime(1970, 1, 1)).total_seconds())


def prepara_mercato(giorno=datetime(2026, 10, 20), movimento=30.0):
    """D1 con escursione di 40 $ (ATR circa 40) e M5 dalle 03:00 alle 09:40 di New York."""
    d1 = [(secondi_broker(giorno - timedelta(days=200 - i)), 4000, 4020, 3980, 4000) for i in range(201)]
    stato.barre[mt5.TIMEFRAME_D1] = np.array(d1, dtype=TIPO_BARRE)
    m5, t = [], giorno.replace(hour=3)
    while t <= giorno.replace(hour=9, minute=45):
        chiusura = 4000 + movimento if t.hour == 9 and t.minute == 40 else 4000
        m5.append((secondi_broker(t), 4000, 4001, 3999, chiusura))
        t += timedelta(minutes=5)
    stato.barre[mt5.TIMEFRAME_M5] = np.array(m5, dtype=TIPO_BARRE)


class ProvaStrategia(unittest.TestCase):
    def test_atr_costante(self):
        self.assertAlmostEqual(atr_wilder([10] * 50, [0] * 50, [5] * 50), 10)

    def test_decisione(self):
        self.assertEqual(decidi(100, 125, 40).direzione, 1)
        self.assertEqual(decidi(100, 75, 40).direzione, -1)
        self.assertEqual(decidi(100, 110, 40).direzione, 0)
        self.assertEqual(decidi(None, 110, 40).direzione, 0)
        self.assertAlmostEqual(decidi(100, 125, 40).distanza_stop, 20)


class ProvaBot(unittest.TestCase):
    def setUp(self):
        self.cartella = tempfile.TemporaryDirectory()
        stato.__init__()
        prepara_mercato()
        cfg = {"controllo": {"simbolo": "XAUUSD"}, "bot": {}}
        with mock.patch.object(principale, "CARTELLA", Path(self.cartella.name)):
            self.bot = principale.Bot(cfg)
        self.bot.avvia()

    def tearDown(self):
        self.bot.r.db.close()
        self.cartella.cleanup()

    def alle(self, ora, minuto, secondo=0):
        t = datetime(2026, 10, 20, ora, minuto, secondo, tzinfo=NEW_YORK)
        stato.ora_tick = secondi_broker(t)
        with mock.patch.object(principale, "adesso_utc", return_value=t.astimezone(timezone.utc)):
            self.bot.giro()

    def test_entra_alle_945_e_chiude_alle_1330(self):
        self.alle(9, 44)
        self.assertEqual(stato.posizioni, [])
        self.alle(9, 45, 10)
        self.assertEqual(len(stato.posizioni), 1)
        p = stato.posizioni[0]
        self.assertEqual(p.type, mt5.ORDER_TYPE_BUY)
        # ATR circa 40 -> stop a 20 $; rischio 750 EUR -> 750 / (20 * 100) = 0,37 lotti
        self.assertAlmostEqual(p.volume, 0.37, places=2)
        self.assertAlmostEqual(stato.ask - p.sl, 20, delta=0.5)
        self.alle(9, 47)  # nessun secondo ordine nello stesso giorno
        self.assertEqual(len(stato.ordini), 1)
        self.alle(13, 29)
        self.assertEqual(len(stato.posizioni), 1)
        self.alle(13, 30, 5)
        self.assertEqual(stato.posizioni, [])
        riga = self.bot.r.db.execute("SELECT motivo, risultato FROM trade").fetchone()
        self.assertEqual(riga, ("orario", 12.0))

    def test_niente_trade_se_movimento_piccolo(self):
        prepara_mercato(movimento=5)
        self.alle(9, 45, 10)
        self.assertEqual(stato.posizioni, [])

    def test_kill_switch_drawdown(self):
        self.alle(9, 0)
        stato.equity = 89_000  # -11% dal picco
        self.alle(9, 45, 10)
        self.assertEqual(stato.posizioni, [])
        self.assertTrue(self.bot.r.leggi("bloccato"))

    def test_stop_scattato_dal_broker(self):
        self.alle(9, 45, 10)
        stato.posizioni = []  # il broker ha chiuso con lo stop
        self.alle(10, 0)
        riga = self.bot.r.db.execute("SELECT motivo FROM trade").fetchone()
        self.assertEqual(riga[0], "stop, target o chiusa fuori dal bot")

    def test_posizione_senza_stop_viene_chiusa(self):
        self.alle(9, 45, 10)
        stato.posizioni[0].sl = 0
        self.alle(9, 50)
        self.assertEqual(stato.posizioni, [])

    def test_rifiuta_conto_reale(self):
        stato.demo = False
        with self.assertRaises(SystemExit):
            self.bot.avvia()


def prepara_indice(simbolo="US500", giorno=datetime(2026, 10, 20), salto=0.0, ora_salto=(10, 25)):
    """15 giornate di M5 dalle 09:30 alle 16:00 NY: ogni giorno il prezzo oscilla di +/-10 punti
    attorno a 5000 (zona di rumore circa 0,2%). Il giorno di prova, dalla barra `ora_salto`,
    il prezzo sale di `salto` punti."""
    m5 = []
    for g in range(15, -1, -1):
        d = giorno - timedelta(days=g)
        if d.weekday() >= 5:
            continue
        t = d.replace(hour=9, minute=30)
        while t < d.replace(hour=16):
            onda = 10.0 if (t.minute // 5) % 2 else -10.0
            chiusura = 5000 + onda + (salto if g == 0 and (t.hour, t.minute) >= ora_salto else 0)
            m5.append((secondi_broker(t), 5000, max(5000, chiusura), min(5000, chiusura), chiusura))
            t += timedelta(minutes=5)
    stato.barre[(simbolo, mt5.TIMEFRAME_M5)] = np.array(m5, dtype=TIPO_BARRE)
    stato.prezzi[simbolo] = (5000 + salto, 5000.5 + salto)


class ProvaZonaDiRumore(unittest.TestCase):
    def setUp(self):
        self.cartella = tempfile.TemporaryDirectory()
        stato.__init__()
        prepara_mercato(movimento=5)  # oro fermo: nessun trade sull'oro
        prepara_indice("US100")
        cfg = {"controllo": {"simbolo": "XAUUSD"}, "bot": {}, "rumore": {"simboli": ["US500", "US100"]}}
        self.patch = mock.patch.object(principale, "CARTELLA", Path(self.cartella.name))
        self.patch.start()
        self.vix = mock.patch("bot.vix.oggi_si_opera", return_value=(True, "VIX alto"))
        self.vix.start()
        self.bot = principale.Bot(cfg)
        self.bot.avvia()

    def tearDown(self):
        self.vix.stop()
        self.patch.stop()
        self.bot.r.db.close()
        self.cartella.cleanup()

    def alle(self, ora, minuto, secondo=0):
        t = datetime(2026, 10, 20, ora, minuto, secondo, tzinfo=NEW_YORK)
        stato.ora_tick = secondi_broker(t)
        with mock.patch.object(principale, "adesso_utc", return_value=t.astimezone(timezone.utc)):
            self.bot.giro()

    def test_dentro_la_zona_nessun_trade(self):
        prepara_indice("US500", salto=0)
        for ora, minuto in [(10, 0), (10, 30), (11, 0)]:
            self.alle(ora, minuto, 5)
        self.assertEqual(stato.posizioni, [])

    def test_fuori_dalla_zona_entra_con_stop_e_target_e_chiude_alle_16(self):
        prepara_indice("US500", salto=60)
        stato.equity = 10_000
        self.alle(10, 0, 5)
        self.assertEqual(stato.posizioni, [])  # alle 10:00 il salto non c'e' ancora
        self.alle(10, 30, 5)
        self.assertEqual(len(stato.posizioni), 1)
        p = stato.posizioni[0]
        self.assertEqual((p.symbol, p.type), ("US500", mt5.ORDER_TYPE_BUY))
        stop = stato.prezzi["US500"][1] - p.sl
        self.assertAlmostEqual(p.tp - stato.prezzi["US500"][1], 2.5 * stop, delta=0.02)
        # rischio 0,5% di 10.000 = 50; 1 punto = 1 $ a lotto
        self.assertAlmostEqual(p.volume * stop, 50, delta=stop * 0.01 + 0.1)
        self.alle(11, 0, 5)
        self.assertEqual(len(stato.ordini), 1)  # gia' in posizione: niente secondo ordine
        self.alle(16, 0, 5)
        self.assertEqual(stato.posizioni, [])
        riga = self.bot.r.db.execute("SELECT simbolo, strategia, motivo FROM trade").fetchone()
        self.assertEqual(riga, ("US500", "zona di rumore", "orario"))

    def test_pausa_dall_apprendimento(self):
        prepara_indice("US500", salto=60)
        cartella_log = Path(self.cartella.name) / "logs"
        (cartella_log / "parametri_rumore.json").write_text('{"US500": {"pausa": true}}')
        self.bot.pausa_su_demo = True
        self.alle(10, 30, 5)
        self.assertEqual(stato.posizioni, [])

    def test_pausa_sul_demo_opera_lo_stesso(self):
        prepara_indice("US500", salto=60)
        cartella_log = Path(self.cartella.name) / "logs"
        (cartella_log / "parametri_rumore.json").write_text('{"US500": {"pausa": true}}')
        self.alle(10, 30, 5)
        self.assertEqual(len(stato.posizioni), 1)
        riga = self.bot.r.db.execute("SELECT strategia FROM trade").fetchone()
        self.assertEqual(riga[0], "zona di rumore (in pausa)")

    def test_massimo_tre_trade_al_giorno(self):
        prepara_indice("US500", salto=60)
        for ora, minuto in [(10, 30), (11, 0), (11, 30), (12, 0), (12, 30)]:
            stato.posizioni = []  # chiuse dallo stop o dal target
            self.alle(ora, minuto, 5)
        self.assertEqual(len(stato.ordini), 3)

    def test_giorno_calmo_niente_trade(self):
        prepara_indice("US500", salto=60)
        with mock.patch("bot.vix.oggi_si_opera", return_value=(False, "VIX basso")):
            self.alle(10, 30, 5)
        self.assertEqual(stato.posizioni, [])

    def test_vix_non_disponibile_opera_e_avvisa(self):
        prepara_indice("US500", salto=60)
        with mock.patch("bot.vix.oggi_si_opera", return_value=(None, "VIX non disponibile")):
            self.alle(10, 30, 5)
        self.assertEqual(len(stato.posizioni), 1)

    def test_ogni_controllo_una_volta_sola(self):
        prepara_indice("US500", salto=60)
        self.alle(10, 30, 5)
        stato.posizioni = []
        self.alle(10, 31)
        self.assertEqual(len(stato.ordini), 1)


class ProvaFiltroVix(unittest.TestCase):
    def test_come_nel_backtest(self):
        import pandas as pd
        from bot import vix
        giorni = pd.bdate_range("2024-01-01", periods=400)
        serie = pd.Series(np.r_[np.full(300, 15.0), np.full(100, 25.0)], index=giorni)
        serie.iloc[350] = 10.0
        with tempfile.TemporaryDirectory() as c, mock.patch.object(vix, "storico", return_value=serie):
            nervosi = vix.giorni_nervosi(serie)
            for i in (299, 300, 301, 351, 352):
                si, _ = vix.oggi_si_opera(Path(c), giorni[i].date())
                self.assertEqual(si, bool(nervosi.iloc[i]), i)


if __name__ == "__main__":
    unittest.main()
