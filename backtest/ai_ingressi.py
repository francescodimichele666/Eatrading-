"""AI che impara dagli errori della zona di rumore e decide quali ingressi prendere.

Per ogni segnale si raccoglie solo cio' che si sapeva in quel momento (VIX di ieri, ora,
quanto il prezzo e' fuori dalla zona, volatilita', giorno prima, apertura, ultimi trade).
Un modello (alberi di decisione, gradient boosting) impara dai trade passati quali
ingressi tendono a finire male. Esame: ogni anno il modello si allena solo sugli anni
prima e decide sull'anno dopo, che non ha mai visto.

Uso: python -m backtest.ai_ingressi <zip US500> <zip NAS100> <vix.csv>
"""

import argparse

import numpy as np
import pandas as pd

from .motore import simula_ordini
from .ricerca import apertura_al_minuto, carica_mercato, ordini, t_stat
from .rumore import ULTIMO_CONTROLLO, USCITA
from .indicatori import RR

CARATTERISTICHE = ["eccesso", "ora", "vol_relativa", "vix", "vix_relativo", "ieri_allineato",
                   "gap_allineato", "direzione", "giorno_settimana", "forma_20"]


def segnali_con_caratteristiche(m, vix: pd.Series, k: float = 1.0, stop: float = 1.0) -> pd.DataFrame:
    apertura = apertura_al_minuto(m, 990)
    controlli = np.arange(990 + 30, ULTIMO_CONTROLLO + 1, 30)
    sel = np.isin(m.minuto + 5, controlli)
    prezzi = pd.DataFrame({"giorno": m.giorno[sel], "minuto": m.minuto[sel] + 5,
                           "close": m.m5["close"].to_numpy()[sel]})
    prezzi = prezzi.pivot_table(index="giorno", columns="minuto", values="close", aggfunc="last")
    apertura = apertura.reindex(prezzi.index)
    scost = prezzi.div(apertura, axis=0) - 1
    sigma = scost.abs().rolling(14, min_periods=10).mean().shift(1)
    eccesso = (scost.abs() / (k * sigma)).stack()
    direzione = np.sign(scost).stack()
    larghezza = (k * sigma).stack()
    df = pd.DataFrame({"eccesso": eccesso, "direzione": direzione, "larghezza": larghezza}).dropna()
    df = df[df["eccesso"] > 1]

    giorni = df.index.get_level_values(0)
    chiusura_ieri = m.d1["close"].shift(1)
    ieri_prima = m.d1["close"].shift(2)
    df["ora"] = df.index.get_level_values(1)
    df["vol_relativa"] = (m.atr_ieri / m.atr_ieri.rolling(250, min_periods=100).median()).reindex(giorni).to_numpy()
    v_ieri = vix.shift(1)
    df["vix"] = v_ieri.reindex(giorni).to_numpy()
    df["vix_relativo"] = (v_ieri / vix.rolling(252, min_periods=200).median().shift(1)).reindex(giorni).to_numpy()
    df["ieri_allineato"] = ((chiusura_ieri / ieri_prima - 1).reindex(giorni).to_numpy()) * df["direzione"]
    df["gap_allineato"] = ((apertura / chiusura_ieri.reindex(apertura.index) - 1).reindex(giorni).to_numpy()) * df["direzione"]
    df["giorno_settimana"] = pd.DatetimeIndex(giorni).dayofweek
    distanza = stop * df["larghezza"].to_numpy() * apertura.reindex(giorni).to_numpy()
    o = ordini(giorni, df["ora"].to_numpy(), df["direzione"].astype(int).to_numpy(), USCITA,
               stop_dist=distanza, target_dist=RR * distanza)
    df.index = pd.MultiIndex.from_arrays([giorni, df["ora"].to_numpy()])
    return o, df


def trade_con_caratteristiche(m, vix) -> pd.DataFrame:
    o, car = segnali_con_caratteristiche(m, vix)
    t = simula_ordini(m.m5, o, 3, m.costi)
    t["data"] = pd.to_datetime(t["giorno"])
    # ogni trade e' entrato all'apertura della barra dell'ora di controllo
    from .ricerca import a_utc
    chiavi = pd.DataFrame({"giorno": car.index.get_level_values(0), "ora": car.index.get_level_values(1)})
    chiavi["entrata_utc"] = a_utc(chiavi["giorno"], chiavi["ora"])
    car = car.reset_index(drop=True).assign(entrata_utc=chiavi["entrata_utc"].to_numpy())
    t = t.merge(car.drop(columns="direzione"), on="entrata_utc", how="left")
    t["forma_20"] = t["R"].rolling(20, min_periods=5).sum().shift(1)
    t["mercato"] = m.nome
    return t


def esame(tutti: pd.DataFrame, primo_anno: int = 2020):
    from sklearn.ensemble import HistGradientBoostingClassifier
    tutti = tutti.dropna(subset=["eccesso"]).copy()
    tutti["anno"] = tutti["data"].dt.year
    tutti["vince"] = (tutti["R"] > 0).astype(int)
    pezzi = []
    for anno in range(primo_anno, tutti["anno"].max() + 1):
        allena = tutti[tutti["anno"] < anno]
        prova = tutti[tutti["anno"] == anno].copy()
        modello = HistGradientBoostingClassifier(max_depth=3, max_iter=150, learning_rate=0.05,
                                                 min_samples_leaf=60, random_state=1)
        modello.fit(allena[CARATTERISTICHE], allena["vince"])
        soglia = np.quantile(modello.predict_proba(allena[CARATTERISTICHE])[:, 1], 0.5)
        prova["probabilita"] = modello.predict_proba(prova[CARATTERISTICHE])[:, 1]
        prova["prende"] = prova["probabilita"] >= soglia
        pezzi.append(prova)
    return pd.concat(pezzi)


def riassunto(r) -> str:
    r = np.asarray(r)
    if len(r) == 0:
        return "nessun trade"
    pf = r[r > 0].sum() / -r[r < 0].sum()
    return f"{len(r)} trade, PF {pf:.2f}, t {t_stat(r):.2f}, {r.sum():+.1f} R"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("zip_sp")
    a.add_argument("zip_nas")
    a.add_argument("vix_csv")
    arg = a.parse_args()
    vix = pd.read_csv(arg.vix_csv, parse_dates=["data"]).set_index("data")["c"]
    tutti = pd.concat([trade_con_caratteristiche(carica_mercato(z), vix) for z in (arg.zip_sp, arg.zip_nas)])
    risultato = esame(tutti)
    risultato["vix_ok"] = risultato["vix_relativo"] > 1
    print("Fuori campione 2020-2026 (S&P + Nasdaq, rischio uguale):")
    for nome, filtro in [("tutti i segnali", slice(None)), ("filtro VIX", risultato["vix_ok"]),
                         ("AI", risultato["prende"]), ("AI + filtro VIX", risultato["prende"] & risultato["vix_ok"])]:
        q = risultato[filtro]
        anni = q.groupby("anno")["R"].sum().round(1).to_dict()
        recenti = q[q["data"] >= "2025-04-01"]["R"]
        print(f"  {nome:16s} {riassunto(q['R'])} | ultimi 18 mesi: {riassunto(recenti)} | anni {anni}")


if __name__ == "__main__":
    main()
