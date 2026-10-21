"""Il bot: gira 24 ore su 24, opera l'idea B sul conto DEMO.

Ogni 10 secondi:
1. controlla il collegamento a MT5 e lo ripristina se serve;
2. aggiorna il kill switch con l'equity del conto;
3. confronta le posizioni reali con quelle che il bot crede di avere;
4. chiude le posizioni arrivate all'orario di uscita (13:30 di New York);
5. alle 09:45 di New York decide se entrare (una volta al giorno).
Ogni ora manda un "sono vivo" su Telegram.

Uso: doppio clic su avvia_bot.bat (oppure: python -m bot.principale).
"""

import sys
import time
import tomllib
from datetime import timedelta
from pathlib import Path

from . import broker
from .orari import a_new_york, adesso_utc, broker_a_utc, new_york
from .registro import Registro
from .rischio import KillSwitch, Limiti
from .strategia_b import ORA_DECISIONE, ORA_INIZIO, ORA_USCITA, atr_wilder, decidi

CARTELLA = Path(__file__).resolve().parent.parent
PAUSA = 10


def carica_config() -> dict:
    file = CARTELLA / "config.toml"
    if not file.exists():
        file = CARTELLA / "config.example.toml"
    with open(file, "rb") as f:
        return tomllib.load(f)


class Bot:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        cfg_bot = cfg.get("bot", {})
        self.soglia = float(cfg_bot.get("soglia_atr", 0.5))
        self.stop = float(cfg_bot.get("stop_atr", 0.5))
        self.limiti = Limiti(rischio_per_trade=float(cfg_bot.get("rischio_per_trade", 0.0075)))
        self.r = Registro(CARTELLA / "logs", cfg.get("telegram", {}))
        self.ks = KillSwitch(self.r, self.limiti, CARTELLA / "logs" / "SBLOCCA.txt")
        self.simbolo = None
        self.ultimo_battito = None
        self.allarme_collegamento = False

    # ---------- avvio e collegamento ----------

    def avvia(self):
        broker.collega(self.cfg.get("mt5", {}))
        c = broker.conto()
        if not c.demo:
            self.r.evento("blocco", "il conto collegato NON e' demo: il bot in questa fase opera "
                                    "solo su demo e si ferma.", avvisa=True)
            broker.scollega()
            sys.exit(2)  # 2 = fermati senza ripartire (vedi avvia_bot.bat)
        self.simbolo = broker.trova_simbolo(self.cfg.get("controllo", {}).get("simbolo", "XAUUSD"))
        self.r.evento("avvio", f"bot avviato su conto demo {c.login} ({c.valuta}), simbolo "
                               f"{self.simbolo}, soglia {self.soglia} ATR, stop {self.stop} ATR, "
                               f"rischio {self.limiti.rischio_per_trade:.2%}", avvisa=True)

    def controlla_collegamento(self) -> bool:
        if broker.collegato():
            if self.allarme_collegamento:
                self.r.evento("collegamento", "collegamento a MT5 ripristinato", avvisa=True)
                self.allarme_collegamento = False
            return True
        if not self.allarme_collegamento:
            self.r.evento("errore", "collegamento a MT5 perso, riprovo ogni minuto", avvisa=True)
            self.allarme_collegamento = True
        try:
            broker.scollega()
            broker.collega(self.cfg.get("mt5", {}))
        except broker.ErroreBroker as errore:
            self.r.log.warning(str(errore))
            time.sleep(50)
        return broker.collegato()

    # ---------- un giro del ciclo ----------

    def giro(self):
        ora = adesso_utc()
        oggi_ny = a_new_york(ora).date()
        c = broker.conto()
        self.ks.aggiorna_equity(c.equity, oggi_ny.isoformat())
        self.riconcilia()
        self.chiudi_a_orario(ora)

        decisione_alle = new_york(oggi_ny, *ORA_DECISIONE) + timedelta(seconds=5)
        if (a_new_york(ora).weekday() < 5 and decisione_alle <= ora < decisione_alle + timedelta(minutes=5)
                and self.r.leggi("deciso_il") != oggi_ny.isoformat()):
            self.r.scrivi("deciso_il", oggi_ny.isoformat())
            self.decidi_e_entra(ora, oggi_ny, c)

        if self.ultimo_battito is None or ora - self.ultimo_battito >= timedelta(hours=1):
            self.ultimo_battito = ora
            aperte = broker.posizioni_del_bot(self.simbolo)
            self.r.evento("battito", f"sono vivo. Equity {c.equity:.2f} {c.valuta}, "
                                     f"posizioni aperte {len(aperte)}", avvisa=True)

    def decidi_e_entra(self, ora, oggi_ny, c):
        barre_m5 = broker.barre(self.simbolo, "M5", 400)
        per_orario = {b["utc"]: b for b in barre_m5}
        b_inizio = per_orario.get(new_york(oggi_ny, *ORA_INIZIO))
        b_decisione = per_orario.get(new_york(oggi_ny, ORA_DECISIONE[0], ORA_DECISIONE[1] - 5))
        d1 = broker.barre(self.simbolo, "D1", 200, da_posizione=1)
        atr = atr_wilder([b["high"] for b in d1], [b["low"] for b in d1], [b["close"] for b in d1])
        d = decidi(b_inizio["open"] if b_inizio else None,
                   b_decisione["close"] if b_decisione else None, atr, self.soglia, self.stop)
        dati = {"prezzo_inizio": b_inizio and b_inizio["open"],
                "prezzo_decisione": b_decisione and b_decisione["close"], "atr": atr}
        if d.direzione == 0:
            self.r.evento("decisione", f"nessun trade oggi: {d.motivo}", avvisa=True, **dati)
            return

        bid, ask, ultimo_tick = broker.prezzo(self.simbolo)
        eta = (ora - ultimo_tick).total_seconds()
        motivo = self.ks.motivo_per_non_entrare(c.equity, ask - bid, eta)
        if motivo:
            self.r.evento("blocco", f"segnale {'long' if d.direzione == 1 else 'short'} ignorato: {motivo}",
                          avvisa=True, **dati)
            return
        entrata = ask if d.direzione == 1 else bid
        stop = entrata - d.direzione * d.distanza_stop
        lotti = broker.lotti_per_rischio(self.simbolo, d.direzione, entrata, stop,
                                         c.equity * self.limiti.rischio_per_trade)
        if lotti <= 0:
            self.r.evento("decisione", "segnale ignorato: anche il lotto minimo rischierebbe troppo",
                          avvisa=True, **dati)
            return
        ticket, prezzo, stop = broker.apri(self.simbolo, d.direzione, lotti, d.distanza_stop, "idea B")
        self.r.trade_aperto(ticket, d.direzione, lotti, prezzo, stop)
        self.r.evento("ordine", f"aperto {'LONG' if d.direzione == 1 else 'SHORT'} {lotti} lotti a "
                                f"{prezzo}, stop {stop}. {d.motivo}", avvisa=True, ticket=ticket, **dati)

    def riconcilia(self):
        reali = {p.ticket: p for p in broker.posizioni_del_bot(self.simbolo)}
        for p in reali.values():
            if p.sl == 0:
                prezzo = broker.chiudi(p, "senza stop")
                self.r.trade_chiuso(p.ticket, prezzo, broker.risultato_posizione(p.ticket), "senza stop")
                self.r.evento("errore", f"posizione {p.ticket} senza stop loss: chiusa a {prezzo}",
                              avvisa=True)
        if len(reali) > 1:
            self.r.evento("errore", f"{len(reali)} posizioni aperte, ne era prevista al massimo una",
                          avvisa=True)
        for ticket in self.r.trade_aperti_registrati():
            if ticket not in reali:
                risultato = broker.risultato_posizione(ticket)
                self.r.trade_chiuso(ticket, None, risultato, "stop o chiusa fuori dal bot")
                self.r.evento("chiusura", f"posizione {ticket} chiusa dal broker (stop), "
                                          f"risultato {risultato:+.2f}", avvisa=True)

    def chiudi_a_orario(self, ora):
        for p in broker.posizioni_del_bot(self.simbolo):
            aperta_ny = a_new_york(broker_a_utc(p.time))
            uscita = new_york(aperta_ny.date(), *ORA_USCITA)
            if ora >= uscita:
                prezzo = broker.chiudi(p, "orario")
                time.sleep(1)
                risultato = broker.risultato_posizione(p.ticket)
                self.r.trade_chiuso(p.ticket, prezzo, risultato, "orario")
                self.r.evento("chiusura", f"posizione {p.ticket} chiusa alle 13:30 di New York a "
                                          f"{prezzo}, risultato {risultato:+.2f}", avvisa=True)

    def gira(self):
        self.avvia()
        while True:
            try:
                if self.controlla_collegamento():
                    self.giro()
            except broker.ErroreBroker as errore:
                self.r.evento("errore", str(errore), avvisa=True)
            except Exception as errore:  # noqa: BLE001 - il bot non deve morire per un errore imprevisto
                self.r.log.exception("errore imprevisto")
                self.r.evento("errore", f"errore imprevisto: {errore!r}", avvisa=True)
                time.sleep(60)
            time.sleep(PAUSA)


if __name__ == "__main__":
    Bot(carica_config()).gira()
