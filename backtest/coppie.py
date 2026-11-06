"""Coppie che si muovono al contrario: EURUSD/USDCHF e AUDUSD/USDCAD.

EURUSD x USDCHF = EURCHF e AUDUSD x USDCAD = AUDCAD: quando le due coppie smettono di
muoversi al contrario, si muove il cross. Due famiglie (regole in
risultati/2026-10-22_indicatori_e_coppie.md):
- divergenza: si scommette che il cross sintetico torni verso la sua media,
  pagando i costi di tutte e due le coppie;
- conferma: si segue il movimento di una coppia solo se l'altra si e' mossa al
  contrario della stessa misura.

Uso: python -m backtest.coppie <zip coppia A> <zip coppia B> [--finale]
     (es. logs/forex_EURUSD.zip logs/forex_USDCHF.zip)
"""

import argparse
from datetime import datetime
from functools import partial
from pathlib import Path

import numpy as np
import pandas as pd

from . import indicatori
from .motore import Costi
from .ricerca import (FINE_SVILUPPO, RISCHIO, Mercato, apertura_al_minuto, apprendimento, carica_mercato,
                      finale, mercato_da, ordini, valuta_famiglia)

RR = indicatori.RR


def cross_sintetico(a: Mercato, b: Mercato) -> Mercato:
    """Barre M5 del prodotto A x B. Il vero massimo del cross dentro la barra non si conosce:
    massimo x massimo lo esagera (le due coppie vanno al contrario), quindi si usano apertura e
    chiusura. Gli stop vengono controllati ogni 5 minuti, a prezzo di chiusura."""
    df = a.m5.join(b.m5, how="inner", lsuffix="_a", rsuffix="_b")
    apertura, chiusura = df["open_a"] * df["open_b"], df["close_a"] * df["close_b"]
    m5 = pd.DataFrame({
        "open": apertura, "high": np.maximum(apertura, chiusura),
        "low": np.minimum(apertura, chiusura), "close": chiusura, "spread": 0.0}, index=df.index)
    prezzo_a, prezzo_b, prezzo = a.m5["close"].iloc[-1], b.m5["close"].iloc[-1], m5["close"].iloc[-1]
    costi = Costi(
        punto=a.costi.punto,
        commissione_oncia=prezzo * (a.costi.commissione_oncia / prezzo_a + b.costi.commissione_oncia / prezzo_b),
        spread_minimo_rel=a.costi.spread_minimo_rel + b.costi.spread_minimo_rel,
        slittamento_rel=a.costi.slittamento_rel + b.costi.slittamento_rel)
    return mercato_da(f"{a.nome}x{b.nome}", m5, costi)


def divergenza(m: Mercato, tf: int, finestra: int, z: float, stop: float, durata):
    """Il cross si e' allontanato dalla sua media di `z` deviazioni: si scommette sul rientro."""
    b = indicatori.barre(m, tf)
    lc = np.log(b["close"])
    zeta = (lc - lc.rolling(finestra).mean()) / lc.rolling(finestra).std()
    rientra_su = (zeta.shift() < -z) & (zeta >= -z)
    rientra_giu = (zeta.shift() > z) & (zeta <= z)
    segnale = np.where(rientra_su, 1, np.where(rientra_giu, -1, 0))
    dist = stop * b["atr"].to_numpy()
    return indicatori._ordini(b, segnale, dist, dist * RR, durata)


def conferma(m: Mercato, altra: Mercato, inizio: int, decisione: int, uscita: int, soglia: float,
             stop: float):
    """Movimento di `m` da `inizio` a `decisione` oltre soglia x ATR, e `altra` mossa al
    contrario oltre soglia x il suo ATR: si segue il movimento di `m`."""
    def movimento(x: Mercato):
        p0, p1 = apertura_al_minuto(x, inizio), apertura_al_minuto(x, decisione)
        return (p1 - p0) / x.atr_ieri
    df = pd.DataFrame({"a": movimento(m), "b": movimento(altra), "atr": m.atr_ieri}).dropna()
    ok = (df["a"].abs() > soglia) & (df["b"].abs() > soglia) & (np.sign(df["a"]) == -np.sign(df["b"]))
    df = df[ok]
    dist = stop * df["atr"]
    return ordini(df.index, decisione, np.sign(df["a"]), uscita, stop_dist=dist, target_dist=RR * dist)


GRIGLIA_DIVERGENZA = {"tf": [15, 60], "finestra": [48, 96], "z": [2.0, 2.5], "stop": [1.0, 1.5, 2.0],
                      "durata": [240, None]}
GRIGLIA_CONFERMA = {"inizio": [90, 600], "decisione": [930, 1005], "uscita": [1230, 1380],
                    "soglia": [0.2, 0.4], "stop": [0.5, 1.0]}


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("zip_a")
    arg.add_argument("zip_b")
    arg.add_argument("--finale", action="store_true", help="apre il cassetto dei 18 mesi")
    a = arg.parse_args()
    ma, mb = carica_mercato(a.zip_a), carica_mercato(a.zip_b)
    cross = cross_sintetico(ma, mb)
    prove_famiglie = [
        (f"divergenza {cross.nome}", cross, divergenza, GRIGLIA_DIVERGENZA, indicatori.MAX_TRADE_GIORNO),
        (f"conferma {ma.nome} con {mb.nome}", ma, partial(conferma, altra=mb), GRIGLIA_CONFERMA, 1),
        (f"conferma {mb.nome} con {ma.nome}", mb, partial(conferma, altra=ma), GRIGLIA_CONFERMA, 1),
    ]
    righe = [f"# Coppie opposte {ma.nome} / {mb.nome} - {datetime.now():%d/%m/%Y %H:%M}", "",
             f"Sviluppo fino al {FINE_SVILUPPO:%d/%m/%Y}. Rischio {RISCHIO:.0%} a trade, take profit "
             f"{RR} volte lo stop. Costi cross: {cross.costi}", ""]
    sintesi, tutte = [], {}
    for nome, m, funzione, griglia, max_trade in prove_famiglie:
        print(f"{nome}...", flush=True)
        s, scelte, prove = valuta_famiglia(m, nome, funzione, griglia, m.m5, max_trade)
        tutte.update({f"{nome} {k}": t for k, t in prove.items()})
        riga = {"famiglia": nome, **{k: s.get(k) for k in [
            "trade", "profit_factor", "R_medio", "t_stat", "anni_in_utile", "griglia_pf_sopra_1_%",
            "drawdown_95%_dei_casi_%", "combinazioni", "supera_sviluppo"]}}
        if a.finale and s["supera_sviluppo"]:
            f = finale(prove, scelte)
            riga.update({"finale_trade": f.get("trade"), "finale_pf": f.get("profit_factor"),
                         "finale_t": f.get("t_stat"), "finale_parametri": f.get("parametri")})
        sintesi.append(riga)
        righe += [f"## {nome}", "", pd.DataFrame([s]).T.to_markdown(), "",
                  "Parametri scelti nel walk-forward:", "", pd.DataFrame(scelte).to_markdown(index=False), ""]
    s, scelte = apprendimento(tutte)
    sintesi.append({"famiglia": "APPRENDIMENTO (sceglie ogni anno tra tutte)", **{k: s.get(k) for k in [
        "trade", "profit_factor", "R_medio", "t_stat", "anni_in_utile", "drawdown_95%_dei_casi_%"]}})
    righe[4:4] = ["## Sintesi", "", pd.DataFrame(sintesi).to_markdown(index=False), ""]
    Path("risultati").mkdir(exist_ok=True)
    file = Path("risultati") / f"coppie_{ma.nome}_{mb.nome}_{datetime.now():%Y%m%d_%H%M}.md"
    file.write_text("\n".join(righe), encoding="utf-8")
    print("\n".join(righe[:12 + len(sintesi)]))
    print(f"\nRapporto: {file}")


if __name__ == "__main__":
    main()
