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
    # Lo spread salvato nelle barre MT5 e' spesso piu' basso del vero (a volte 0).
    # Minimo: 0,09 $ misurati dal vivo con l'oro a 4136 $, in proporzione al prezzo.
    spread_minimo_rel: float = 0.09 / 4136
    # Slittamento su entrate a mercato e stop: 0,10 $ a 4136 $, in proporzione.
    slittamento_rel: float = 0.10 / 4136


def simula(percorso: pd.DataFrame, segnali: pd.DataFrame, p: Parametri,
           c: Costi = Costi()) -> pd.DataFrame:
    tempi = percorso.index
    apertura = percorso["open"].to_numpy()
    massimo = percorso["high"].to_numpy()
    minimo = percorso["low"].to_numpy()
    chiusura = percorso["close"].to_numpy()
    spread = np.maximum(percorso["spread"].to_numpy() * c.punto,
                        apertura * c.spread_minimo_rel)
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
        slittamento = apertura[i] * c.slittamento_rel
        distanza_stop = p.stop_atr * s["atr"]
        if d == 1:
            entrata = apertura[i] + spread[i] + slittamento
        else:
            entrata = apertura[i] - slittamento
        stop = entrata - d * distanza_stop
        target = entrata + d * p.target_atr * s["atr"]

        uscita, motivo, j = None, None, i
        while j < len(tempi):
            if giorno_it[j] != s["giorno"] or minuti_it[j] >= p.ora_chiusura * 60:
                uscita, motivo = (apertura[j] if d == 1 else apertura[j] + spread[j]), "orario"
                break
            if d == 1:
                if minimo[j] <= stop:
                    uscita, motivo = min(stop, apertura[j]) - slittamento, "stop"
                    break
                if massimo[j] >= target:
                    uscita, motivo = target, "target"
                    break
            else:
                if massimo[j] + spread[j] >= stop:
                    uscita, motivo = max(stop, apertura[j] + spread[j]) + slittamento, "stop"
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
    valori = {
        "trade": len(r),
        "vincenti_%": round(100 * (r > 0).mean(), 1),
        "R_medio": round(r.mean(), 3),
        "R_totale": round(r.sum(), 1),
        "profit_factor": round(vinti / persi, 2) if persi else float("inf"),
        "rendimento_%": round(100 * (capitale[-1] - 1), 1),
        "drawdown_max_%": round(100 * (1 - capitale / picco).max(), 1),
    }
    return {k: float(v) if isinstance(v, np.floating) else v for k, v in valori.items()}


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


def simula_ordini(percorso: pd.DataFrame, ordini: pd.DataFrame, max_trade_giorno: int,
                  c: Costi = Costi()) -> pd.DataFrame:
    """Versione generale di `simula`: ogni ordine porta con se' stop, target e
    orario di uscita. Colonne di `ordini` (indice = momento della decisione, UTC):
    direzione, stop_prezzo o stop_dist, target_dist (NaN = nessun target),
    scadenza (UTC), giorno; facoltativa trail_dist (stop che segue il prezzo di chiusura
    a quella distanza, solo a favore). Si entra all'apertura della prima barra successiva."""
    tempi = percorso.index
    apertura = percorso["open"].to_numpy()
    massimo = percorso["high"].to_numpy()
    minimo = percorso["low"].to_numpy()
    chiusura = percorso["close"].to_numpy()
    spread = np.maximum(percorso["spread"].to_numpy() * c.punto, apertura * c.spread_minimo_rel)

    trade = []
    libero_da = tempi[0]
    per_giorno: dict = {}
    for tempo, o in ordini.iterrows():
        if tempo < libero_da or per_giorno.get(o["giorno"], 0) >= max_trade_giorno:
            continue
        i = tempi.searchsorted(tempo)
        fine = tempi.searchsorted(o["scadenza"])
        if i >= fine or fine >= len(tempi):
            continue
        d = int(o["direzione"])
        slittamento = apertura[i] * c.slittamento_rel
        entrata = apertura[i] + spread[i] + slittamento if d == 1 else apertura[i] - slittamento
        stop = o["stop_prezzo"] if pd.notna(o.get("stop_prezzo")) else entrata - d * o["stop_dist"]
        rischio = d * (entrata - stop)
        if rischio <= 0:
            continue  # il prezzo ha gia' superato lo stop
        target = entrata + d * o["target_dist"] if pd.notna(o.get("target_dist")) else None
        segui = o["trail_dist"] if pd.notna(o.get("trail_dist", np.nan)) else None

        uscita, motivo, j = None, None, i
        for j in range(i, fine + 1):
            if j == fine:
                uscita, motivo = (apertura[j] if d == 1 else apertura[j] + spread[j]), "orario"
                break
            if d == 1:
                if minimo[j] <= stop:
                    uscita, motivo = min(stop, apertura[j]) - slittamento, "stop"
                    break
                if target is not None and massimo[j] >= target:
                    uscita, motivo = target, "target"
                    break
            else:
                if massimo[j] + spread[j] >= stop:
                    uscita, motivo = max(stop, apertura[j] + spread[j]) + slittamento, "stop"
                    break
                if target is not None and minimo[j] + spread[j] <= target:
                    uscita, motivo = target, "target"
                    break
            if segui is not None:  # aggiornato a barra chiusa: vale dalla barra dopo
                stop = max(stop, chiusura[j] - segui) if d == 1 else min(stop, chiusura[j] + segui)

        risultato = d * (uscita - entrata) - c.commissione_oncia
        trade.append({"entrata_utc": tempi[i], "uscita_utc": tempi[j], "direzione": d,
                      "prezzo_entrata": round(entrata, 2), "prezzo_uscita": round(uscita, 2),
                      "dollari_oncia": round(risultato, 2), "R": risultato / rischio,
                      "motivo": motivo, "giorno": o["giorno"]})
        per_giorno[o["giorno"]] = per_giorno.get(o["giorno"], 0) + 1
        libero_da = tempi[min(j + 1, len(tempi) - 1)]
    return pd.DataFrame(trade)
