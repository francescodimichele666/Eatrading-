"""Momentum fuori dalla "zona di rumore" (Zarattini, Aziz, Barbon, "Beat the Market: An
Effective Intraday Momentum Strategy for S&P500 ETF (SPY)", Swiss Finance Institute 24-97, 2024).

Idea: ogni giorno, a ogni ora del giorno, il prezzo si allontana dall'apertura di una certa
quantita' "normale" (la media delle ultime 14 giornate a quella stessa ora). Finche' resta
dentro quella zona e' rumore. Se ne esce, c'e' qualcuno che sta comprando o vendendo
davvero, e si segue il movimento fino a fine giornata.

Regole (scritte prima del test, vedi risultati/2026-10-22_zona_di_rumore.md):
- apertura di riferimento alle 03:00 NY (Londra) oppure alle 09:30 NY (Wall Street);
- controllo ogni 30 minuti fino alle 15:30 NY; uscita al piu' tardi alle 16:00 NY;
- zona = apertura x (1 +/- k x media degli scostamenti delle ultime 14 giornate a quell'ora);
- stop a m volte la larghezza della zona; uscita "rr" = take profit a 2,5 volte lo stop
  (regola di Francesco), uscita "segui" = stop che segue il prezzo, come nello studio;
- al massimo 3 trade al giorno, uno alla volta.
"""

import numpy as np
import pandas as pd

from .indicatori import RR
from .ricerca import Mercato, apertura_al_minuto, ordini

ULTIMO_CONTROLLO = 1350  # 15:30 NY
USCITA = 1380            # 16:00 NY


def zona_di_rumore(m: Mercato, inizio: int, k: float, stop: float, uscita: str):
    apertura = apertura_al_minuto(m, inizio)
    controlli = np.arange(inizio + 30, ULTIMO_CONTROLLO + 1, 30)
    sel = np.isin(m.minuto + 5, controlli)  # barra M5 che chiude all'ora del controllo
    prezzi = pd.DataFrame({"giorno": m.giorno[sel], "minuto": m.minuto[sel] + 5,
                           "close": m.m5["close"].to_numpy()[sel]})
    prezzi = prezzi.pivot_table(index="giorno", columns="minuto", values="close", aggfunc="last")
    apertura = apertura.reindex(prezzi.index)
    scostamento = (prezzi.div(apertura, axis=0) - 1).abs()
    sigma = scostamento.rolling(14, min_periods=10).mean().shift(1)  # solo giornate passate

    alto = (1 + k * sigma).mul(apertura, axis=0)
    basso = (1 - k * sigma).mul(apertura, axis=0)
    segnale = np.where(prezzi > alto, 1, np.where(prezzi < basso, -1, 0))
    segnale = pd.DataFrame(segnale, index=prezzi.index, columns=prezzi.columns)
    segnale = segnale.where(sigma.notna(), 0).stack()
    larghezza = (k * sigma).mul(apertura, axis=0).stack().reindex(segnale.index)
    segnale = segnale[segnale != 0]
    larghezza = larghezza.loc[segnale.index]

    giorni = segnale.index.get_level_values(0)
    minuti = segnale.index.get_level_values(1).to_numpy()
    distanza = stop * larghezza.to_numpy()
    if uscita == "rr":
        return ordini(giorni, minuti, segnale.to_numpy(), USCITA, stop_dist=distanza,
                      target_dist=RR * distanza)
    return ordini(giorni, minuti, segnale.to_numpy(), USCITA, stop_dist=distanza, trail_dist=distanza)


FAMIGLIE = {
    "zona_di_rumore": (zona_di_rumore, {
        "inizio": [600, 990], "k": [1.0, 1.5], "stop": [0.5, 1.0], "uscita": ["rr", "segui"]}),
}
MAX_TRADE_GIORNO = 3
