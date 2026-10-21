"""Simulazione dei trade barra per barra, con spread, commissioni e slittamento.

I prezzi di MT5 sono BID. Un long compra all'ASK (bid + spread) ed esce al
bid; uno short vende al bid ed esce all'ASK. Se nella stessa barra vengono
toccati sia lo stop sia il target, contiamo lo stop (ipotesi prudente).
Il risultato di ogni trade e' in "R": 1R = la perdita se scatta lo stop.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .strategia import FUSO_ITALIA, Parametri


@dataclass(frozen=True)
class Costi:
    punto: float = 0.01                 # XAUUSD.r: 2 decimali
    commissione_oncia: float = 0.07     # circa 7 $ a lotto (100 once) andata e ritorno
    slittamento: float = 0.10           # $ persi su entrate a mercato e stop


def simula(percorso: pd.DataFrame, segnali: pd.DataFrame, p: Parametri,
           c: Costi = Costi()) -> pd.DataFrame:
    tempi = percorso.index
    apertura = percorso["open"].to_numpy()
    massimo = percorso["high"].to_numpy()
    minimo = percorso["low"].to_numpy()
    spread = percorso["spread"].to_numpy() * c.punto
    ora_it = tempi.tz_convert(FUSO_ITALIA)
    minuti_it = ora_it.hour * 60 + ora_it.minute
    giorno_it = ora_it.tz_localize(None).normalize()

    trade = []
    libero_da = tempi[0]
    conteggio: dict = {}
    for tempo, s in segnali.iterrows():
        if tempo < libero_da:
            continue
        stato = conteggio.setdefault(s["giorno"], {"n": 0, "perdite": 0})
        if stato["n"] >= p.max_trade_giorno or stato["perdite"] >= p.max_perdite_consecutive:
            continue
        i = tempi.searchsorted(tempo)
        if i >= len(tempi) or giorno_it[i] != s["giorno"] or minuti_it[i] >= p.ora_chiusura * 60:
            continue

        d = int(s["direzione"])
        distanza_stop = p.stop_atr * s["atr"]
        if d == 1:
            entrata = apertura[i] + spread[i] + c.slittamento
        else:
            entrata = apertura[i] - c.slittamento
        stop = entrata - d * distanza_stop
        target = entrata + d * p.target_atr * s["atr"]

        uscita, motivo, j = None, None, i
        while j < len(tempi):
            if giorno_it[j] != s["giorno"] or minuti_it[j] >= p.ora_chiusura * 60:
                uscita, motivo = (apertura[j] if d == 1 else apertura[j] + spread[j]), "orario"
                break
            if d == 1:
                if minimo[j] <= stop:
                    uscita, motivo = min(stop, apertura[j]) - c.slittamento, "stop"
                    break
                if massimo[j] >= target:
                    uscita, motivo = target, "target"
                    break
            else:
                if massimo[j] + spread[j] >= stop:
                    uscita, motivo = max(stop, apertura[j] + spread[j]) + c.slittamento, "stop"
                    break
                if minimo[j] + spread[j] <= target:
                    uscita, motivo = target, "target"
                    break
            j += 1
        if uscita is None:
            break  # fine dei dati

        risultato = d * (uscita - entrata) - c.commissione_oncia
        r = risultato / distanza_stop
        trade.append({"entrata_utc": tempi[i], "uscita_utc": tempi[min(j, len(tempi) - 1)],
                      "direzione": d, "prezzo_entrata": round(entrata, 2),
                      "prezzo_uscita": round(uscita, 2), "dollari_oncia": round(risultato, 2),
                      "R": r, "motivo": motivo, "giorno": s["giorno"]})
        stato["n"] += 1
        stato["perdite"] = stato["perdite"] + 1 if r < 0 else 0
        libero_da = tempi[min(j + 1, len(tempi) - 1)]
    return pd.DataFrame(trade)


def statistiche(trade: pd.DataFrame, rischio: float = 0.0075) -> dict:
    if trade.empty:
        return {"trade": 0}
    r = trade["R"].to_numpy()
    vinti, persi = r[r > 0].sum(), -r[r < 0].sum()
    capitale = np.cumprod(1 + rischio * r)
    picco = np.maximum.accumulate(np.concatenate([[1.0], capitale]))[1:]
    return {
        "trade": len(r),
        "vincenti_%": round(100 * (r > 0).mean(), 1),
        "R_medio": round(r.mean(), 3),
        "R_totale": round(r.sum(), 1),
        "profit_factor": round(vinti / persi, 2) if persi else float("inf"),
        "rendimento_%": round(100 * (capitale[-1] - 1), 1),
        "drawdown_max_%": round(100 * (1 - capitale / picco).max(), 1),
    }


def per_anno(trade: pd.DataFrame, rischio: float = 0.0075) -> pd.DataFrame:
    if trade.empty:
        return pd.DataFrame()
    anni = pd.DatetimeIndex(trade["giorno"]).year
    return pd.DataFrame({a: statistiche(t, rischio) for a, t in trade.groupby(anni)}).T


def monte_carlo(trade: pd.DataFrame, rischio: float = 0.0075, prove: int = 2000,
                seme: int = 1) -> dict:
    """Rimescola l'ordine dei trade per stimare il drawdown peggiore realistico."""
    if len(trade) < 20:
        return {}
    gen = np.random.default_rng(seme)
    r = trade["R"].to_numpy()
    cali = []
    for _ in range(prove):
        capitale = np.cumprod(1 + rischio * gen.permutation(r))
        picco = np.maximum.accumulate(np.concatenate([[1.0], capitale]))[1:]
        cali.append((1 - capitale / picco).max())
    return {"drawdown_mediano_%": round(float(100 * np.median(cali)), 1),
            "drawdown_95%_dei_casi_%": round(float(100 * np.quantile(cali, 0.95)), 1)}
