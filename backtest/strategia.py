"""Regole della strategia MVP: bias macro del giorno + ritracciamento su M15.

Ogni funzione usa solo informazioni disponibili PRIMA del momento della
decisione, per non "sbirciare il futuro" nel backtest.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

FUSO_ITALIA = "Europe/Rome"


@dataclass(frozen=True)
class Parametri:
    media_bias: int = 20          # giorni della media per tassi reali e DXY
    media_m15: int = 20           # periodi della media mobile su M15
    periodi_atr: int = 14
    tolleranza_atr: float = 0.25  # quanto vicino alla media deve arrivare il prezzo, in ATR
    stop_atr: float = 1.5
    target_atr: float = 2.0
    ora_inizio: int = 9           # ora italiana, prima entrata possibile
    ora_fine_entrate: int = 18
    ora_chiusura: int = 21        # tutto chiuso entro quest'ora
    max_trade_giorno: int = 3
    max_perdite_consecutive: int = 2
    usa_bias: bool = True         # False = opera in entrambe le direzioni (confronto)
    blocco_nfp: bool = True


# Pesi ufficiali ICE del Dollar Index
PESI_DXY = {"EURUSD": -0.576, "USDJPY": 0.136, "GBPUSD": -0.119,
            "USDCAD": 0.091, "USDSEK": 0.042, "USDCHF": 0.036}


def dxy_sintetico(cambi_d1: dict[str, pd.DataFrame]) -> pd.Series | None:
    if not all(c in cambi_d1 for c in PESI_DXY):
        return None
    chiusure = pd.DataFrame({c: cambi_d1[c]["close"] for c in PESI_DXY}).dropna()
    valore = 50.14348112 * np.prod([chiusure[c] ** p for c, p in PESI_DXY.items()], axis=0)
    return pd.Series(valore, index=chiusure.index, name="DXY")


def bias_giornaliero(giorni: pd.DatetimeIndex, tasso_reale: pd.Series,
                     dollaro: pd.Series, p: Parametri) -> pd.Series:
    """+1 = solo long, -1 = solo short, 0 = fermo, per ogni giorno di trading.

    Tasso reale: FRED pubblica il dato di un giorno nel pomeriggio americano
    del giorno lavorativo dopo, quindi alle 8:30 italiane di D usiamo il dato
    di due giorni lavorativi prima. Dollaro: barra giornaliera chiusa il giorno prima.
    """
    def segno(serie: pd.Series) -> pd.DataFrame:
        s = np.sign(serie - serie.rolling(p.media_bias).mean()).dropna()
        s = s.rename("segno").rename_axis("data").reset_index()
        s["data"] = s["data"].astype("datetime64[ns]")
        return s

    giorni_df = pd.DataFrame({"giorno": giorni.astype("datetime64[ns]")})
    giorni_df["data_tasso"] = giorni_df["giorno"] - pd.offsets.BDay(2)
    giorni_df["data_dollaro"] = giorni_df["giorno"] - pd.Timedelta(days=1)
    giorni_df["data_tasso"] = giorni_df["data_tasso"].astype("datetime64[ns]")

    tasso = pd.merge_asof(giorni_df.sort_values("data_tasso"), segno(tasso_reale),
                          left_on="data_tasso", right_on="data")["segno"].to_numpy()
    dollaro_s = pd.merge_asof(giorni_df.sort_values("data_dollaro"), segno(dollaro),
                              left_on="data_dollaro", right_on="data")["segno"].to_numpy()
    # Oro sale quando tasso reale e dollaro scendono insieme
    bias = np.where((tasso < 0) & (dollaro_s < 0), 1, np.where((tasso > 0) & (dollaro_s > 0), -1, 0))
    return pd.Series(bias, index=giorni)


def barre_m15(m5: pd.DataFrame) -> pd.DataFrame:
    m15 = m5.resample("15min", label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "spread": "max"}
    ).dropna(subset=["open"])
    return m15


def atr(df: pd.DataFrame, periodi: int) -> pd.Series:
    chiusura_prec = df["close"].shift()
    vero = pd.concat([df["high"] - df["low"], (df["high"] - chiusura_prec).abs(),
                      (df["low"] - chiusura_prec).abs()], axis=1).max(axis=1)
    return vero.ewm(alpha=1 / periodi, adjust=False).mean()


def giorno_nfp(orari_ny: pd.DatetimeIndex) -> np.ndarray:
    """Primo venerdi' del mese, 7:45-9:15 di New York (dato alle 8:30).
    Approssimazione: il calendario storico vero arrivera' con la Fase 2."""
    primo_venerdi = (orari_ny.dayofweek == 4) & (orari_ny.day <= 7)
    minuti = orari_ny.hour * 60 + orari_ny.minute
    return primo_venerdi & (minuti >= 7 * 60 + 45) & (minuti <= 9 * 60 + 15)


def segnali(m5: pd.DataFrame, bias: pd.Series | None, p: Parametri) -> pd.DataFrame:
    """Un segnale alla chiusura di una barra M15: prezzo tornato verso la media
    nella direzione del bias e candela di rifiuto. L'entrata avviene alla barra dopo."""
    m15 = barre_m15(m5)
    media = m15["close"].rolling(p.media_m15).mean()
    volat = atr(m15, p.periodi_atr)
    chiusura_barra = m15.index + pd.Timedelta(minutes=15)
    ora_it = chiusura_barra.tz_convert(FUSO_ITALIA)
    giorno = ora_it.tz_localize(None).normalize()

    corpo = (m15["close"] - m15["low"]) / (m15["high"] - m15["low"]).replace(0, np.nan)
    long_ok = ((m15["low"] <= media + p.tolleranza_atr * volat) & (m15["close"] > media)
               & (m15["close"] > m15["open"]) & (corpo >= 0.5))
    short_ok = ((m15["high"] >= media - p.tolleranza_atr * volat) & (m15["close"] < media)
                & (m15["close"] < m15["open"]) & (corpo <= 0.5))

    if p.usa_bias and bias is not None:
        b = bias.reindex(giorno).to_numpy()
        long_ok &= b == 1
        short_ok &= b == -1

    finestra = (ora_it.hour >= p.ora_inizio) & (ora_it.hour < p.ora_fine_entrate)
    if p.blocco_nfp:
        finestra &= ~giorno_nfp(chiusura_barra.tz_convert("America/New_York"))

    direzione = np.where(long_ok & finestra, 1, np.where(short_ok & finestra, -1, 0))
    out = pd.DataFrame({"direzione": direzione, "atr": volat.to_numpy(), "giorno": giorno},
                       index=chiusura_barra)
    return out[(out["direzione"] != 0) & out["atr"].notna()]
