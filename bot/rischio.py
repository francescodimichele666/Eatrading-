"""Kill switch: le regole che fermano il bot prima che faccia danni.

Il blocco per drawdown totale resta attivo anche dopo un riavvio: si toglie
solo a mano, creando il file logs/SBLOCCA.txt dopo aver capito cosa e'
successo (vedi README). Il bot lo legge, toglie il blocco e lo cancella.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Limiti:
    rischio_per_trade: float = 0.0075   # 0,75% dell'equity
    perdita_giornaliera_max: float = 0.02
    drawdown_max: float = 0.10
    spread_max: float = 0.50            # dollari; dal vivo il mediano era 0,09
    eta_prezzo_max: float = 120         # secondi senza nuovi prezzi = dati vecchi


class KillSwitch:
    def __init__(self, registro, limiti: Limiti, file_sblocco: Path):
        self.r = registro
        self.limiti = limiti
        self.file_sblocco = file_sblocco

    def aggiorna_equity(self, equity: float, giorno: str):
        picco = max(self.r.leggi("picco_equity", equity), equity)
        self.r.scrivi("picco_equity", picco)
        if self.r.leggi("giorno") != giorno:
            self.r.scrivi("giorno", giorno)
            self.r.scrivi("equity_inizio_giorno", equity)

        if self.file_sblocco.exists() and self.r.leggi("bloccato"):
            self.file_sblocco.unlink()
            self.r.scrivi("bloccato", None)
            self.r.scrivi("picco_equity", equity)
            self.r.evento("sblocco", "blocco tolto a mano, picco azzerato all'equity attuale", avvisa=True)

        if not self.r.leggi("bloccato") and equity < picco * (1 - self.limiti.drawdown_max):
            motivo = (f"drawdown oltre il {self.limiti.drawdown_max:.0%}: equity {equity:.2f}, "
                      f"picco {picco:.2f}")
            self.r.scrivi("bloccato", motivo)
            self.r.evento("blocco", motivo + ". Il bot non apre piu' trade finche' non lo sblocchi.",
                          avvisa=True)

    def motivo_per_non_entrare(self, equity: float, spread: float, eta_prezzo: float) -> str | None:
        bloccato = self.r.leggi("bloccato")
        if bloccato:
            return f"bot bloccato: {bloccato}"
        inizio = self.r.leggi("equity_inizio_giorno", equity)
        if equity < inizio * (1 - self.limiti.perdita_giornaliera_max):
            return f"perdita del giorno oltre il {self.limiti.perdita_giornaliera_max:.0%}"
        if spread > self.limiti.spread_max:
            return f"spread anomalo: {spread:.2f} $"
        if eta_prezzo > self.limiti.eta_prezzo_max:
            return f"prezzi fermi da {eta_prezzo:.0f} secondi"
        return None
