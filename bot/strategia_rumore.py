"""Zona di rumore sugli indici USA: la decisione, senza MT5.

Stesse regole del backtest (backtest/rumore.py, apertura 09:30 NY, k 1, stop 1, uscita "rr"):
- apertura del giorno = apertura della barra M5 delle 09:30 di New York;
- alle 10:00, 10:30, ... 15:30 si guarda la chiusura della barra M5 appena finita;
- zona = apertura x (1 +/- k x sigma), dove sigma e' la media di quanto il prezzo si era
  allontanato dall'apertura, alla stessa ora, nelle ultime 14 giornate (almeno 10 valori);
- fuori dalla zona si entra nella direzione del movimento, stop a `stop` volte la
  larghezza della zona, take profit a `rr` volte lo stop; tutto chiuso alle 16:00.
"""

from dataclasses import dataclass
from datetime import date, timedelta

from .orari import a_new_york

APERTURA = (9, 30)
CONTROLLI = [(10 + i // 2, 30 * (i % 2)) for i in range(12)]  # 10:00 ... 15:30
USCITA = (16, 0)
GIORNATE = 14
MINIMO_GIORNATE = 10
MAX_TRADE_GIORNO = 3


@dataclass(frozen=True)
class Segnale:
    direzione: int          # +1 long, -1 short, 0 nessun trade
    distanza_stop: float
    distanza_target: float
    motivo: str


def per_giorno(barre: list[dict]) -> dict[date, dict]:
    """Per ogni giorno di New York: apertura delle 09:30 e chiusure agli orari di controllo."""
    giorni: dict[date, dict] = {}
    for b in barre:
        ny = a_new_york(b["utc"])
        g = giorni.setdefault(ny.date(), {"apertura": None, "chiusure": {}})
        if (ny.hour, ny.minute) == APERTURA:
            g["apertura"] = b["open"]
        fine = ny + timedelta(minutes=5)  # la barra chiude 5 minuti dopo l'inizio
        if (fine.hour, fine.minute) in CONTROLLI:
            g["chiusure"][(fine.hour, fine.minute)] = b["close"]
    return giorni


def sigma(giorni: dict[date, dict], oggi: date, controllo: tuple) -> float | None:
    passati = [g for d, g in sorted(giorni.items()) if d < oggi and g["chiusure"]][-GIORNATE:]
    valori = [abs(g["chiusure"][controllo] / g["apertura"] - 1) for g in passati
              if g["apertura"] and controllo in g["chiusure"]]
    return sum(valori) / len(valori) if len(valori) >= MINIMO_GIORNATE else None


def decidi(barre: list[dict], oggi: date, controllo: tuple, k: float = 1.0, stop: float = 1.0,
           rr: float = 2.5) -> Segnale:
    giorni = per_giorno(barre)
    g = giorni.get(oggi)
    if not g or g["apertura"] is None:
        return Segnale(0, 0.0, 0.0, "manca la barra delle 09:30 (festivo?)")
    prezzo = g["chiusure"].get(controllo)
    if prezzo is None:
        return Segnale(0, 0.0, 0.0, f"manca la barra che chiude alle {controllo[0]}:{controllo[1]:02d}")
    s = sigma(giorni, oggi, controllo)
    if s is None:
        return Segnale(0, 0.0, 0.0, "meno di 10 giornate di storico")
    apertura = g["apertura"]
    larghezza = k * s * apertura
    if abs(prezzo - apertura) <= larghezza:
        return Segnale(0, 0.0, 0.0, f"dentro la zona: {prezzo - apertura:+.2f} su +/-{larghezza:.2f}")
    direzione = 1 if prezzo > apertura else -1
    distanza = stop * larghezza
    return Segnale(direzione, distanza, rr * distanza,
                   f"fuori dalla zona: {prezzo - apertura:+.2f} oltre +/-{larghezza:.2f}")
