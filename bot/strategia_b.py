"""Idea B, momentum all'apertura di New York: la decisione, senza MT5.

Stesse regole del backtest (backtest/idee.py, idea_b):
- alle 09:45 di New York si misura il movimento dall'apertura delle 03:00;
- se supera `soglia` volte l'ATR giornaliero (14 giorni, fino a ieri) si entra
  nella stessa direzione, stop a `stop` volte l'ATR, nessun target;
- uscita alle 13:30 di New York.
Tenerla separata da MT5 permette di confrontarla con il backtest.
"""

from dataclasses import dataclass

ORA_INIZIO = (3, 0)       # apertura di Londra, ora di New York
ORA_DECISIONE = (9, 45)   # ora di New York
ORA_USCITA = (13, 30)     # chiusura del COMEX, ora di New York


@dataclass(frozen=True)
class Decisione:
    direzione: int        # +1 long, -1 short, 0 nessun trade
    distanza_stop: float  # in dollari
    motivo: str


def atr_wilder(massimi, minimi, chiusure, periodi: int = 14) -> float:
    """ATR come nel backtest (media esponenziale con alfa 1/periodi)."""
    valore = None
    for i in range(len(chiusure)):
        intervallo = massimi[i] - minimi[i]
        if i > 0:
            intervallo = max(intervallo, abs(massimi[i] - chiusure[i - 1]),
                             abs(minimi[i] - chiusure[i - 1]))
        valore = intervallo if valore is None else valore + (intervallo - valore) / periodi
    return valore


def decidi(prezzo_inizio: float | None, prezzo_decisione: float | None,
           atr_giornaliero: float | None, soglia: float = 0.5, stop: float = 0.5) -> Decisione:
    if prezzo_inizio is None or prezzo_decisione is None:
        return Decisione(0, 0.0, "mancano le barre delle 03:00 o delle 09:40 (festivo?)")
    if not atr_giornaliero or atr_giornaliero <= 0:
        return Decisione(0, 0.0, "ATR giornaliero non disponibile")
    movimento = prezzo_decisione - prezzo_inizio
    if abs(movimento) <= soglia * atr_giornaliero:
        return Decisione(0, 0.0, f"movimento {movimento:+.2f} $ sotto la soglia "
                                 f"{soglia * atr_giornaliero:.2f} $")
    direzione = 1 if movimento > 0 else -1
    return Decisione(direzione, stop * atr_giornaliero,
                     f"movimento {movimento:+.2f} $ oltre la soglia {soglia * atr_giornaliero:.2f} $")
