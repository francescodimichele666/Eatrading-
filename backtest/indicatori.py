"""Strategie classiche a indicatori, versione intraday (sempre flat entro le 16:00 NY).

Regole scritte prima dei test (vedi risultati/2026-10-22_indicatori_e_coppie.md):
- un indicatore per tipo (trend, oscillatore, volatilita'), niente doppioni;
- stop in multipli dell'ATR(14) del timeframe di lavoro, take profit a 2,5 volte lo stop;
- entrate solo tra le 18:30 e le 16:00 NY (minuti 90-1380), come nel resto della ricerca;
- il segnale si legge a barra chiusa e si entra all'apertura della barra M5 dopo.
"""

import numpy as np
import pandas as pd

from .dati import ORE_BROKER_SU_NEW_YORK
from .ricerca import NY, Mercato, ordini
from .strategia import atr

FINE_GIORNATA = 1380


def barre(m: Mercato, minuti: int) -> pd.DataFrame:
    """Barre M15 o H1 ricavate dalle M5, con giornata e minuto di sessione della chiusura."""
    b = m.m5.resample(f"{minuti}min", label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}).dropna()
    chiusura = b.index + pd.Timedelta(minutes=minuti)
    ora_broker = chiusura.tz_convert(NY).tz_localize(None) + pd.Timedelta(hours=ORE_BROKER_SU_NEW_YORK)
    b["giorno"] = ora_broker.normalize()
    b["minuto"] = ora_broker.hour * 60 + ora_broker.minute
    b["atr"] = atr(b, 14)
    return b


def _ordini(b: pd.DataFrame, segnale: np.ndarray, stop_dist, target_dist, durata):
    sel = segnale != 0
    s = b[sel]
    minuto = s["minuto"].to_numpy()
    uscita = np.full(len(s), FINE_GIORNATA) if durata is None else np.minimum(minuto + durata, FINE_GIORNATA)
    ok = minuto < uscita
    stop = np.asarray(stop_dist, dtype=float)[sel][ok]
    target = None if target_dist is None else np.asarray(target_dist, dtype=float)[sel][ok]
    return ordini(s["giorno"].to_numpy()[ok], minuto[ok], segnale[sel][ok], uscita[ok],
                  stop_dist=stop, target_dist=target)


def incrocio(veloce: pd.Series, lenta: pd.Series) -> np.ndarray:
    sopra = (veloce > lenta).astype(int)
    return (sopra.diff().fillna(0)).to_numpy().astype(int)  # +1 incrocio al rialzo, -1 al ribasso


def trend_ema(m: Mercato, tf: int, medie: tuple, stop: float, target: float, durata):
    """Filtro EMA200: solo long sopra, solo short sotto. Entrata all'incrocio EMA veloce/lenta.
    Stop = stop x ATR; target = target x stop (0 = nessun target, si esce a orario)."""
    b = barre(m, tf)
    c = b["close"]
    ema200 = c.ewm(span=200, adjust=False).mean()
    x = incrocio(c.ewm(span=medie[0], adjust=False).mean(), c.ewm(span=medie[1], adjust=False).mean())
    segnale = np.where((x == 1) & (c > ema200), 1, np.where((x == -1) & (c < ema200), -1, 0))
    dist = stop * b["atr"].to_numpy()
    return _ordini(b, segnale, dist, dist * target if target else None, durata)


def bollinger(m: Mercato, tf: int, k: float, oscillatore: str, stop: float, target: float, durata):
    """Ritorno alla media: prezzo sotto la banda bassa negli ultimi 3 barre e oscillatore che
    risale da ipervenduto (Stocastico 14,3 sopra 20, oppure RSI 14 sopra 30). Simmetrico per lo short.
    Target = target x stop (regola di Francesco: 2,5)."""
    b = barre(m, tf)
    c = b["close"]
    media = c.rolling(20).mean()
    dev = c.rolling(20).std(ddof=0)
    alta, bassa = media + k * dev, media - k * dev
    if oscillatore == "stoc":
        minimo, massimo = b["low"].rolling(14).min(), b["high"].rolling(14).max()
        osc = (100 * (c - minimo) / (massimo - minimo)).rolling(3).mean()
        basso, alto = 20, 80
    else:
        delta = c.diff()
        su = delta.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
        giu = (-delta.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
        osc = 100 - 100 / (1 + su / giu)
        basso, alto = 30, 70
    toccata_bassa = (b["low"] <= bassa).rolling(3).max() == 1
    toccata_alta = (b["high"] >= alta).rolling(3).max() == 1
    risale = (osc.shift() < basso) & (osc >= basso)
    scende = (osc.shift() > alto) & (osc <= alto)
    segnale = np.where(toccata_bassa & risale, 1, np.where(toccata_alta & scende, -1, 0))
    dist = stop * b["atr"].to_numpy()
    return _ordini(b, segnale, dist, dist * target, durata)


def ichimoku(m: Mercato, tf: int, segnale_tipo: str, stop: float, target: float, durata):
    """Ichimoku 9/26/52. "incrocio": Tenkan incrocia Kijun con il prezzo dalla parte giusta
    della nuvola. "kumo": il prezzo esce dalla nuvola con Tenkan dalla parte giusta di Kijun."""
    b = barre(m, tf)
    c = b["close"]
    def centro(n):
        return (b["high"].rolling(n).max() + b["low"].rolling(n).min()) / 2
    tenkan, kijun = centro(9), centro(26)
    # la nuvola di oggi e' quella calcolata 26 barre fa
    span_a, span_b = ((tenkan + kijun) / 2).shift(26), centro(52).shift(26)
    sopra_nuvola, sotto_nuvola = c > np.maximum(span_a, span_b), c < np.minimum(span_a, span_b)
    if segnale_tipo == "incrocio":
        x = incrocio(tenkan, kijun)
        segnale = np.where((x == 1) & sopra_nuvola, 1, np.where((x == -1) & sotto_nuvola, -1, 0))
    else:
        esce_su = sopra_nuvola & ~sopra_nuvola.shift(fill_value=False)
        esce_giu = sotto_nuvola & ~sotto_nuvola.shift(fill_value=False)
        segnale = np.where(esce_su & (tenkan > kijun), 1, np.where(esce_giu & (tenkan < kijun), -1, 0))
    dist = stop * b["atr"].to_numpy()
    return _ordini(b, segnale, dist, dist * target if target else None, durata)


GIORNATA = None  # durata None = si esce alle 16:00 NY
RR = 2.5  # regola di Francesco: take profit a 2,5 volte il rischio

FAMIGLIE = {
    "trend_ema": (trend_ema, {
        "tf": [15, 60], "medie": [(9, 21), (20, 50)], "stop": [1.0, 1.5, 2.0],
        "target": [RR], "durata": [240, GIORNATA]}),
    "bollinger": (bollinger, {
        "tf": [15, 60], "k": [2.0, 2.5], "oscillatore": ["stoc", "rsi"], "stop": [1.0, 1.5, 2.0],
        "target": [RR], "durata": [240, GIORNATA]}),
    "ichimoku": (ichimoku, {
        "tf": [15, 60], "segnale_tipo": ["incrocio", "kumo"], "stop": [1.0, 1.5, 2.0],
        "target": [RR], "durata": [240, GIORNATA]}),
}
MAX_TRADE_GIORNO = 3
