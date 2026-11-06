"""Strategie intraday pubblicate, provate con le regole scritte prima del test
(vedi risultati/2026-10-22_strategie_pubblicate.md).

Orari in minuti di sessione (dalle 17:00 NY): 02:00 NY = 540, 08:00 = 900, 09:30 = 990,
10:00 = 1020, 11:00 = 1080, 14:00 = 1260, 15:30 = 1350, 16:00 = 1380.
"""

import numpy as np
import pandas as pd

from .indicatori import RR
from .ricerca import Mercato, apertura_al_minuto, ordini


def _chiusura_al_minuto(m: Mercato, minuto: int) -> pd.Series:
    """Chiusura della barra M5 che inizia a `minuto` (quindi il prezzo a minuto + 5)."""
    sel = m.minuto == minuto
    return pd.Series(m.m5["close"].to_numpy()[sel], index=m.giorno[sel]).groupby(level=0).last()


def _barra(m: Mercato, minuto: int) -> pd.DataFrame:
    sel = m.minuto == minuto
    return pd.DataFrame({c: m.m5[c].to_numpy()[sel] for c in ("open", "high", "low", "close")},
                        index=m.giorno[sel]).groupby(level=0).last()


def orb(m: Mercato, target: float):
    """Zarattini e Aziz (2023), "Can Day Trading Really Be Profitable?": la prima candela
    M5 dopo le 09:30 NY da' la direzione; si entra alle 09:35, stop all'estremo opposto
    della candela, take profit a `target` volte il rischio, altrimenti uscita alle 16:00."""
    b = _barra(m, 990)
    b = b[b["close"] != b["open"]]
    d = np.sign(b["close"] - b["open"]).astype(int)
    stop = np.where(d == 1, b["low"], b["high"])
    rischio = (b["close"] - stop).abs()
    return ordini(b.index, 995, d, 1380, stop_prezzo=stop, target_dist=target * rischio)


def ultima_mezzora(m: Mercato, segnale: str, stop: float):
    """Gao, Han, Li e Zhou (2018, Journal of Financial Economics), "Market intraday momentum":
    il rendimento dalla chiusura di ieri (16:00) alle 10:00 prevede l'ultima mezz'ora.
    "r1": si segue il suo segno dalle 15:30 alle 16:00. "r1_e_r12": solo se anche il
    rendimento 15:00-15:30 ha lo stesso segno. Stop di sicurezza a `stop` x ATR giornaliero."""
    ieri = _chiusura_al_minuto(m, 1375).shift(1)
    alle_10 = _chiusura_al_minuto(m, 1015)
    alle_15 = _chiusura_al_minuto(m, 1315)
    alle_1530 = _chiusura_al_minuto(m, 1345)
    df = pd.DataFrame({"ieri": ieri, "r10": alle_10, "r15": alle_15, "r1530": alle_1530,
                       "atr": m.atr_ieri}).dropna()
    d = np.sign(df["r10"] - df["ieri"])
    if segnale == "r1_e_r12":
        d = d.where(np.sign(df["r1530"] - df["r15"]) == d, 0)
    return ordini(df.index, 1350, d.astype(int), 1380, stop_dist=stop * df["atr"])


# segno del trade che COMPRA la valuta che non e' nelle sue ore di mercato:
# finestra -> {coppia: direzione}
ORE_LOCALI = {
    # Breedon e Ranaldo: le valute europee si indeboliscono nelle ore europee...
    "europa": (540, 900, {"EURUSD": -1, "USDCHF": 1}),
    # ...e il dollaro nelle ore americane
    "america": (1020, 1380, {"EURUSD": 1, "USDCHF": -1, "AUDUSD": 1}),
    # il dollaro australiano nelle ore asiatiche (19:00-02:00 NY)
    "asia": (120, 540, {"AUDUSD": -1}),
}


def ore_locali(m: Mercato, finestra: str, stop: float):
    """Breedon e Ranaldo (Banca Nazionale Svizzera, 2011), "Intraday patterns in FX returns
    and order flow": una valuta tende a perdere valore durante le ore del suo mercato."""
    da, a, versi = ORE_LOCALI[finestra]
    verso = next((v for coppia, v in versi.items() if m.nome.startswith(coppia)), 0)
    giorni = m.atr_ieri.dropna().index
    giorni = giorni[pd.DatetimeIndex(giorni).dayofweek < 5]
    return ordini(giorni, da, np.full(len(giorni), verso), a, stop_dist=stop * m.atr_ieri.loc[giorni].to_numpy())


DOLLARO = {"EURUSD": -1, "USDCHF": 1, "AUDUSD": -1, "USDCAD": 1}


def fixing(m: Mercato, fase: str, stop: float):
    """Krohn, Mueller e Whelan (Journal of Finance, 2024), "Foreign exchange fixings and
    returns around the clock": il dollaro si rafforza nelle ore prima del fixing di Londra
    (16:00 di Londra = 11:00 NY) e si indebolisce dopo. "prima": dollaro long 08:00-11:00 NY;
    "dopo": dollaro short 11:00-14:00 NY."""
    verso = next((v for coppia, v in DOLLARO.items() if m.nome.startswith(coppia)), 0)
    da, a, segno = (900, 1080, 1) if fase == "prima" else (1080, 1260, -1)
    giorni = m.atr_ieri.dropna().index
    giorni = giorni[pd.DatetimeIndex(giorni).dayofweek < 5]
    return ordini(giorni, da, np.full(len(giorni), verso * segno), a,
                  stop_dist=stop * m.atr_ieri.loc[giorni].to_numpy())


FAMIGLIE_INDICI = {
    "orb_zarattini": (orb, {"target": [RR, 10.0]}),
    "ultima_mezzora_gao": (ultima_mezzora, {"segnale": ["r1", "r1_e_r12"], "stop": [0.5, 1.0]}),
}
FAMIGLIE_FOREX = {
    "ore_locali_breedon": (ore_locali, {"finestra": ["europa", "america", "asia"], "stop": [0.5, 1.0]}),
    "fixing_krohn": (fixing, {"fase": ["prima", "dopo"], "stop": [0.5, 1.0]}),
}
