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
        self.assertEqual(riga[0], "stop o chiusa fuori dal bot")

    def test_posizione_senza_stop_viene_chiusa(self):
        self.alle(9, 45, 10)
        stato.posizioni[0].sl = 0
        self.alle(9, 50)
        self.assertEqual(stato.posizioni, [])

    def test_rifiuta_conto_reale(self):
        stato.demo = False
        with self.assertRaises(SystemExit):
            self.bot.avvia()


if __name__ == "__main__":
    unittest.main()
