"""Le tre idee intraday di risultati/2026-10-21_ipotesi_intraday.md.

Uso: python -m backtest.idee dati_backtest_AAAAMMGG.zip
"""

import itertools
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

from .dati import ORE_BROKER_SU_NEW_YORK, carica
from .motore import Costi, monte_carlo, per_anno, simula_ordini, statistiche
from .strategia import FUSO_ITALIA, atr

NY = "America/New_York"
ANNI_ALLENAMENTO = 3


def giorno_broker(indice: pd.DatetimeIndex) -> pd.DatetimeIndex:
    """La giornata del broker cambia alle 17:00 di New York."""
    ora = indice.tz_convert(NY).tz_localize(None) + pd.Timedelta(hours=ORE_BROKER_SU_NEW_YORK)
    return ora.normalize()


def barre_giornaliere(m5: pd.DataFrame) -> pd.DataFrame:
    return m5.groupby(giorno_broker(m5.index)).agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"})


def valore_fino_a_ieri(giorni: pd.DatetimeIndex, serie: pd.Series) -> np.ndarray:
    """Per ogni giorno, l'ultimo valore giornaliero di un giorno precedente."""
    sx = pd.DataFrame({"g": giorni.astype("datetime64[ns]") - pd.Timedelta(days=1)})
    dx = serie.dropna().rename("v").rename_axis("g").reset_index()
    dx["g"] = dx["g"].astype("datetime64[ns]")
    return pd.merge_asof(sx, dx, on="g")["v"].to_numpy()


def _ordini(righe: list[dict]) -> pd.DataFrame:
    if not righe:
        return pd.DataFrame(columns=["direzione", "stop_prezzo", "stop_dist", "target_dist",
                                     "scadenza", "giorno"])
    df = pd.DataFrame(righe).set_index("tempo").sort_index()
    for col in ["stop_prezzo", "stop_dist", "target_dist"]:
        if col not in df:
            df[col] = np.nan
    return df


# ---------- Idea A: rottura del range notturno all'apertura di Londra ----------

def idea_a(m5: pd.DataFrame, atr_d1: pd.Series, stop: str = "opposto", target: float = 1.0):
    it = m5.index.tz_convert(FUSO_ITALIA)
    giorno = it.tz_localize(None).normalize()
    ora = it.hour
    chiusura_barra = m5.index + pd.Timedelta(minutes=5)
    ora_chiusura = chiusura_barra.tz_convert(FUSO_ITALIA)
    minuti_chiusura = ora_chiusura.hour * 60 + ora_chiusura.minute

    notte = (ora >= 1) & (ora < 8)
    rng = m5[notte].groupby(giorno[notte]).agg(alto=("high", "max"), basso=("low", "min"))
    rng["atr"] = valore_fino_a_ieri(pd.DatetimeIndex(rng.index), atr_d1)
    rng = rng[(rng["alto"] - rng["basso"]) <= rng["atr"]]

    finestra = (minuti_chiusura > 9 * 60) & (minuti_chiusura <= 12 * 60)
    candidati = pd.DataFrame({"close": m5["close"].to_numpy(), "giorno": giorno,
                              "tempo": chiusura_barra})[finestra]
    candidati = candidati.join(rng, on="giorno", how="inner")
    rottura = np.where(candidati["close"] > candidati["alto"], 1,
                       np.where(candidati["close"] < candidati["basso"], -1, 0))
    candidati = candidati[rottura != 0].assign(direzione=rottura[rottura != 0])
    prime = candidati.groupby("giorno").head(1)

    righe = []
    for _, r in prime.iterrows():
        altezza = r["alto"] - r["basso"]
        if stop == "opposto":
            livello = r["basso"] if r["direzione"] == 1 else r["alto"]
        else:
            livello = (r["alto"] + r["basso"]) / 2
        scadenza = (r["giorno"] + pd.Timedelta(hours=21)).tz_localize(FUSO_ITALIA).tz_convert("UTC")
        righe.append({"tempo": r["tempo"], "direzione": r["direzione"], "stop_prezzo": livello,
                      "target_dist": target * altezza, "scadenza": scadenza, "giorno": r["giorno"]})
    return _ordini(righe)


# ---------- Idea B: momentum all'apertura di New York ----------

def idea_b(m5: pd.DataFrame, atr_d1: pd.Series, soglia: float = 0.5, stop: float = 0.5):
    ny = m5.index.tz_convert(NY)
    giorno_ny = ny.tz_localize(None).normalize()
    minuti = ny.hour * 60 + ny.minute
    apertura_londra = m5["open"][minuti == 3 * 60].groupby(giorno_ny[minuti == 3 * 60]).first()
    alle_945 = minuti == 9 * 60 + 40  # barra 9:40-9:45, chiude alle 9:45
    prezzo_945 = m5["close"][alle_945].groupby(giorno_ny[alle_945]).first()
    df = pd.DataFrame({"inizio": apertura_londra, "ora": prezzo_945}).dropna()
    df["atr"] = valore_fino_a_ieri(pd.DatetimeIndex(df.index), atr_d1)
    df = df.dropna()
    movimento = df["ora"] - df["inizio"]
    df = df[movimento.abs() > soglia * df["atr"]]

    righe = []
    for g, r in df.iterrows():
        base = pd.Timestamp(g).tz_localize(NY)
        giorno_it = (base + pd.Timedelta(hours=9, minutes=45)).tz_convert(FUSO_ITALIA)
        righe.append({"tempo": (base + pd.Timedelta(hours=9, minutes=45)).tz_convert("UTC"),
                      "direzione": int(np.sign(r["ora"] - r["inizio"])),
                      "stop_dist": stop * r["atr"],
                      "scadenza": (base + pd.Timedelta(hours=13, minutes=30)).tz_convert("UTC"),
                      "giorno": giorno_it.tz_localize(None).normalize()})
    return _ordini(righe)


# ---------- Idea C: rottura H1 nella direzione del trend giornaliero ----------

def idea_c(m5: pd.DataFrame, chiusure_d1: pd.Series, barre: int = 20, stop: float = 2.0):
    h1 = m5.resample("1h", label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}).dropna()
    volat = atr(h1, 14)
    massimo_prec = h1["high"].rolling(barre).max().shift()
    minimo_prec = h1["low"].rolling(barre).min().shift()
    chiusura_barra = h1.index + pd.Timedelta(hours=1)
    it = chiusura_barra.tz_convert(FUSO_ITALIA)
    giorno = it.tz_localize(None).normalize()

    sopra_media = np.sign(chiusure_d1 - chiusure_d1.rolling(50).mean())
    trend = valore_fino_a_ieri(giorno, sopra_media)

    finestra = (it.hour >= 9) & (it.hour <= 18)
    long_ok = (h1["close"].to_numpy() > massimo_prec.to_numpy()) & (trend == 1)
    short_ok = (h1["close"].to_numpy() < minimo_prec.to_numpy()) & (trend == -1)
    direzione = np.where(long_ok & finestra, 1, np.where(short_ok & finestra, -1, 0))

    df = pd.DataFrame({"direzione": direzione, "stop_dist": stop * volat.to_numpy(),
                       "target_dist": 3 * volat.to_numpy(), "giorno": giorno},
                      index=chiusura_barra)
    df = df[(df["direzione"] != 0) & df["stop_dist"].notna()]
    df["scadenza"] = [(g + pd.Timedelta(hours=21)).tz_localize(FUSO_ITALIA).tz_convert("UTC")
                      for g in df["giorno"]]
    df["stop_prezzo"] = np.nan
    return df


IDEE = {
    "A - rottura del range notturno all'apertura di Londra":
        (idea_a, {"stop": ["opposto", "meta"], "target": [1.0, 1.5, 2.0]},
         {"stop": "opposto", "target": 1.0}, 1),
    "B - momentum all'apertura di New York":
        (idea_b, {"soglia": [0.3, 0.5, 0.7], "stop": [0.3, 0.5, 0.7]},
         {"soglia": 0.5, "stop": 0.5}, 1),
    "C - rottura H1 nella direzione del trend giornaliero":
        (idea_c, {"barre": [10, 20, 40], "stop": [1.5, 2.0, 3.0]},
         {"barre": 20, "stop": 2.0}, 2),
}


def soglia_superata(s: dict, anni: pd.DataFrame, mc: dict) -> bool:
    if s.get("trade", 0) < 100 or anni.empty:
        return False
    anni_utili = (anni["R_totale"] > 0).mean()
    return (s["profit_factor"] >= 1.15 and anni_utili >= 0.6
            and mc.get("drawdown_95%_dei_casi_%", 100) < 25)


def main():
    dati = carica(sys.argv[1])
    m5 = dati.oro_m5
    d1 = barre_giornaliere(m5)
    atr_d1 = atr(d1, 14)
    righe = [f"# Tre idee intraday su XAUUSD - {datetime.now():%d/%m/%Y %H:%M}", "",
             f"Dati {m5.index[0]:%d/%m/%Y} - {m5.index[-1]:%d/%m/%Y}, simulazione su M5. "
             "Regole in 2026-10-21_ipotesi_intraday.md.", ""]
    sintesi = []
    for nome, (funzione, griglia, base, max_giorno) in IDEE.items():
        primo = d1["close"] if funzione is idea_c else atr_d1
        prove = {}
        for valori in itertools.product(*griglia.values()):
            parametri = dict(zip(griglia, valori))
            t = simula_ordini(m5, funzione(m5, primo, **parametri), max_giorno)
            if not t.empty:
                t["anno"] = pd.DatetimeIndex(t["giorno"]).year
            prove[valori] = t
        t_base = prove[tuple(base.values())]

        anni = sorted({a for t in prove.values() if not t.empty for a in t["anno"].unique()})
        fuori, scelte = [], []
        for anno in anni[ANNI_ALLENAMENTO:]:
            def punti(v):
                t = prove[v]
                allen = t[(t["anno"] >= anno - ANNI_ALLENAMENTO) & (t["anno"] < anno)] if not t.empty else t
                return allen["R"].sum() if len(allen) >= 30 else float("-inf")
            migliore = max(prove, key=punti)
            t = prove[migliore]
            fuori.append(t[t["anno"] == anno])
            scelte.append({"anno": anno, **dict(zip(griglia, migliore))})
        oos = pd.concat(fuori) if fuori else pd.DataFrame()
        s_oos, a_oos, mc = statistiche(oos), per_anno(oos), monte_carlo(oos)
        passa = soglia_superata(s_oos, a_oos, mc)
        senza_costi = simula_ordini(m5, funzione(m5, primo, **base), max_giorno,
                                    Costi(commissione_oncia=0, spread_minimo_rel=0, slittamento_rel=0))
        sintesi.append({"idea": nome[0], **{k: s_oos.get(k) for k in
                        ["trade", "profit_factor", "R_medio", "drawdown_max_%"]},
                        "anni_in_utile": f"{int((a_oos['R_totale'] > 0).sum())}/{len(a_oos)}" if not a_oos.empty else "-",
                        "MC_95%": mc.get("drawdown_95%_dei_casi_%"), "soglia": "SI" if passa else "no"})
        righe += [f"## {nome}", "",
                  "Regole base:", "", pd.DataFrame([statistiche(t_base)]).to_markdown(index=False), "",
                  f"Regole base senza costi: {statistiche(senza_costi)}", "",
                  "Walk-forward (solo anni di prova):", "",
                  pd.DataFrame([s_oos]).to_markdown(index=False), "",
                  a_oos.to_markdown() if not a_oos.empty else "", "",
                  f"Monte Carlo: {mc}", "",
                  "Parametri scelti:", "", pd.DataFrame(scelte).to_markdown(index=False), "",
                  f"**Soglia per la demo superata: {'SI' if passa else 'NO'}**", ""]
    righe[4:4] = ["## Sintesi (walk-forward)", "", pd.DataFrame(sintesi).to_markdown(index=False), ""]
    Path("risultati").mkdir(exist_ok=True)
    file = Path("risultati") / f"{datetime.now():%Y-%m-%d}_tre_idee_intraday.md"
    file.write_text("\n".join(str(r) for r in righe), encoding="utf-8")
    print("\n".join(str(r) for r in righe))


if __name__ == "__main__":
    main()
