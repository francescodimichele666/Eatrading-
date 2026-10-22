"""Ricerca sistematica di strategie intraday, con difese contro l'overfitting.

Regole (decise prima di guardare i risultati):
- periodo di sviluppo: fino al 31/03/2025; gli ultimi ~18 mesi (dal 01/04/2025)
  restano chiusi e si usano UNA volta sola, alla fine, per i candidati;
- dentro lo sviluppo, walk-forward annuale: 3 anni per scegliere i parametri,
  1 anno di prova mai visto;
- per passare allo "sportello finale" una famiglia deve avere, negli anni di
  prova: almeno 150 trade, profit factor >= 1,20, t-stat del risultato medio
  >= 2,5 (piu' severa del solito perche' proviamo molte famiglie), almeno il
  60% degli anni in utile, e almeno meta' delle combinazioni della griglia
  con profit factor > 1 sull'intero sviluppo (robustezza ai parametri).

Orari: "minuti di sessione" dalle 17:00 di New York (inizio della giornata del
broker). 03:00 NY = 600, 08:20 NY = 920, 09:30 NY = 990, 13:30 NY = 1230.
Niente entrate prima delle 18:30 NY (minuto 90) ne' uscite dopo le 16:00 NY
(minuto 1380): attorno alla chiusura e riapertura giornaliera lo spread vero e'
molto piu' largo di quello salvato nelle barre, e il backtest sarebbe falso.

Uso: python -m backtest.ricerca <zip dati oro o forex> [--finale]
"""

import argparse
import itertools
import json
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

from .dati import ORE_BROKER_SU_NEW_YORK, _barre, ora_broker_a_utc
from .motore import Costi, monte_carlo, per_anno, simula_ordini, statistiche
from .strategia import atr

FINE_SVILUPPO = pd.Timestamp("2025-04-01")
ANNI_ALLENAMENTO = 3
NY = "America/New_York"
MINUTO_PRIMA_ENTRATA = 90
MINUTO_ULTIMA_USCITA = 1380
RISCHIO = 0.01  # regola di Francesco: al massimo 1% del conto per trade


# ------------------------------------------------------------------ dati

@dataclass
class Mercato:
    nome: str
    m5: pd.DataFrame
    costi: Costi
    giorno: np.ndarray          # giornata del broker di ogni barra
    minuto: np.ndarray          # minuti di sessione di ogni barra
    d1: pd.DataFrame            # barre per giornata del broker
    atr_ieri: pd.Series         # ATR giornaliero fino al giorno prima


def carica_mercato(percorso: str) -> Mercato:
    with zipfile.ZipFile(percorso) as z:
        nomi = z.namelist()
        nome_m5 = next(n for n in nomi if n.endswith("_M5.csv.gz"))
        m5 = _barre(z, nome_m5, intraday=True)
        regole = json.loads(z.read("regole.json")) if "regole.json" in nomi else {}
    simbolo = nome_m5.removeprefix("mt5_").removesuffix("_M5.csv.gz")
    m5 = m5[m5.index >= "2017-07-01"]
    regole.setdefault("spread_barre", float(m5["spread"].iloc[-75_000:].median()))
    return mercato_da(simbolo, m5, costi_per(simbolo, regole, float(m5["close"].iloc[-1])))


def mercato_da(simbolo: str, m5: pd.DataFrame, costi: Costi) -> Mercato:
    ora_broker = m5.index.tz_convert(NY).tz_localize(None) + pd.Timedelta(hours=ORE_BROKER_SU_NEW_YORK)
    giorno = ora_broker.normalize()
    minuto = (ora_broker.hour * 60 + ora_broker.minute).to_numpy()
    d1 = m5.groupby(giorno).agg({"open": "first", "high": "max", "low": "min", "close": "last"})
    return Mercato(simbolo, m5, costi, giorno.to_numpy(), minuto, d1, atr(d1, 14).shift(1))


def costi_per(simbolo: str, regole: dict, prezzo_finale: float) -> Costi:
    if simbolo.startswith("XAU"):
        return Costi()
    punto = regole.get("punto", 0.001 if "JPY" in simbolo else 0.00001)
    contratto = regole.get("contratto", 100_000)
    prezzo = regole.get("prezzo") or prezzo_finale
    spread = regole.get("spread_vivo") or regole.get("spread_barre", 10) * punto
    if spread >= 8 * punto:
        # conto standard (simbolo senza .r): il costo del broker e' gia' tutto nello spread
        commissione = 0.0
    else:
        # conto raw: circa 7 $ a lotto andata e ritorno, convertiti nella valuta del prezzo
        commissione = 7.0 / contratto * (prezzo if simbolo[3:6] != "USD" else 1)
        spread = max(spread, 2 * punto)
    # slittamento: 0,2 pip a ogni entrata e a ogni stop
    return Costi(punto=punto, commissione_oncia=commissione,
                 spread_minimo_rel=spread / prezzo, slittamento_rel=2 * punto / prezzo)


def a_utc(giorni, minuti) -> pd.DatetimeIndex:
    ora_ny = pd.to_datetime(giorni) + pd.to_timedelta(np.asarray(minuti) - ORE_BROKER_SU_NEW_YORK * 60, unit="min")
    return pd.DatetimeIndex(ora_ny).tz_localize(NY, ambiguous="NaT", nonexistent="shift_forward").tz_convert("UTC")


def apertura_al_minuto(m: Mercato, minuto: int) -> pd.Series:
    sel = m.minuto == minuto
    return pd.Series(m.m5["open"].to_numpy()[sel], index=m.giorno[sel]).groupby(level=0).first()


def intervallo(m: Mercato, da: int, a: int) -> pd.DataFrame:
    sel = (m.minuto >= da) & (m.minuto < a)
    df = pd.DataFrame({"alto": m.m5["high"].to_numpy()[sel], "basso": m.m5["low"].to_numpy()[sel]},
                      index=m.giorno[sel])
    return df.groupby(level=0).agg({"alto": "max", "basso": "min"})


def ordini(giorni, minuti_entrata, direzione, minuti_uscita, stop_dist=None, stop_prezzo=None,
           target_dist=None) -> pd.DataFrame:
    giorni = pd.DatetimeIndex(giorni)
    n = len(giorni)
    df = pd.DataFrame({
        "direzione": np.asarray(direzione, dtype=int),
        "stop_dist": np.full(n, np.nan) if stop_dist is None else np.asarray(stop_dist, dtype=float),
        "stop_prezzo": np.full(n, np.nan) if stop_prezzo is None else np.asarray(stop_prezzo, dtype=float),
        "target_dist": np.full(n, np.nan) if target_dist is None else np.asarray(target_dist, dtype=float),
        "scadenza": a_utc(giorni, np.broadcast_to(minuti_uscita, n)),
        "giorno": giorni,
    }, index=a_utc(giorni, np.broadcast_to(minuti_entrata, n)))
    entrata_ok = np.broadcast_to(minuti_entrata, n) >= MINUTO_PRIMA_ENTRATA
    uscita_ok = np.broadcast_to(minuti_uscita, n) <= MINUTO_ULTIMA_USCITA
    df = df[(df["direzione"] != 0) & df.index.notna() & df["scadenza"].notna() & entrata_ok & uscita_ok]
    return df[df["stop_dist"].notna() | df["stop_prezzo"].notna()].sort_index()


# ------------------------------------------------------------------ famiglie

def momento(m: Mercato, inizio: int, decisione: int, uscita: int, soglia: float, stop: float,
            verso: int):
    """Movimento da `inizio` a `decisione`: se supera soglia*ATR si segue (verso=+1)
    o si va contro (verso=-1). Comprende l'idea B (600, 1005, 1230, 0.5, 0.5, +1)."""
    p0, p1 = apertura_al_minuto(m, inizio), apertura_al_minuto(m, decisione)
    df = pd.DataFrame({"p0": p0, "p1": p1, "atr": m.atr_ieri}).dropna()
    mov = df["p1"] - df["p0"]
    df = df[mov.abs() > soglia * df["atr"]]
    return ordini(df.index, decisione, verso * np.sign(df["p1"] - df["p0"]), uscita,
                  stop_dist=stop * df["atr"])


def rottura_range(m: Mercato, da: int, a: int, fine_entrate: int, uscita: int, stop: str,
                  target: float, verso: int):
    """Range tra `da` e `a`; prima chiusura M5 fuori dal range entro `fine_entrate`.
    verso=+1 segue la rottura, -1 la sfuma (scommette sul rientro)."""
    rng = intervallo(m, da, a).join(m.atr_ieri.rename("atr")).dropna()
    rng = rng[(rng["alto"] - rng["basso"]) <= rng["atr"]]
    sel = (m.minuto >= a) & (m.minuto < fine_entrate)
    c = pd.DataFrame({"close": m.m5["close"].to_numpy()[sel], "minuto": m.minuto[sel] + 5},
                     index=m.giorno[sel]).join(rng, how="inner")
    lato = np.where(c["close"] > c["alto"], 1, np.where(c["close"] < c["basso"], -1, 0))
    c = c[lato != 0].assign(lato=lato[lato != 0])
    c = c[~c.index.duplicated(keep="first")]
    altezza = c["alto"] - c["basso"]
    d = verso * c["lato"]
    if verso == 1:
        livello = np.where(stop == "opposto", np.where(d == 1, c["basso"], c["alto"]),
                           (c["alto"] + c["basso"]) / 2)
    else:  # sfumare: stop oltre il prezzo di rottura di mezzo range
        livello = np.where(d == 1, c["close"] - 0.5 * altezza, c["close"] + 0.5 * altezza)
    return ordini(c.index, c["minuto"].to_numpy(), d, uscita, stop_prezzo=livello,
                  target_dist=target * altezza if target else None)


def ora_fissa(m: Mercato, entrata: int, durata: int, verso: int, stop: float):
    """Stagionalita' oraria: stessa direzione ogni giorno, da `entrata` per `durata` minuti."""
    giorni = m.atr_ieri.dropna().index
    giorni = giorni[pd.DatetimeIndex(giorni).dayofweek < 5]
    return ordini(giorni, entrata, np.full(len(giorni), verso), entrata + durata,
                  stop_dist=stop * m.atr_ieri.loc[giorni].to_numpy())


def massimo_ieri(m: Mercato, fine_entrate: int, uscita: int, stop: float, verso: int):
    """Rottura del massimo/minimo di ieri tra le 03:00 NY e `fine_entrate`."""
    ieri = m.d1[["high", "low"]].shift(1).join(m.atr_ieri.rename("atr")).dropna()
    sel = (m.minuto >= 600) & (m.minuto < fine_entrate)
    c = pd.DataFrame({"close": m.m5["close"].to_numpy()[sel], "minuto": m.minuto[sel] + 5},
                     index=m.giorno[sel]).join(ieri, how="inner")
    lato = np.where(c["close"] > c["high"], 1, np.where(c["close"] < c["low"], -1, 0))
    c = c[lato != 0].assign(lato=lato[lato != 0])
    c = c[~c.index.duplicated(keep="first")]
    return ordini(c.index, c["minuto"].to_numpy(), verso * c["lato"], uscita,
                  stop_dist=stop * c["atr"])


FAMIGLIE = {
    "momento_o_rientro": (momento, {
        "inizio": [90, 600, 900], "decisione": [930, 1005, 1080], "uscita": [1170, 1230, 1380],
        "soglia": [0.0, 0.3, 0.6], "stop": [0.5, 1.0], "verso": [1, -1]}),
    "rottura_range": (rottura_range, {
        "da,a": [(180, 600), (600, 660), (920, 980), (990, 1020)],
        "fine_entrate": [180], "uscita": [1230, 1380], "stop": ["opposto", "meta"],
        "target": [0, 1.0, 2.0], "verso": [1, -1]}),
    "ora_fissa": (ora_fissa, {
        "entrata": list(range(90, 1380, 120)), "durata": [60, 120, 240],
        "verso": [1, -1], "stop": [1.0]}),
    "massimo_ieri": (massimo_ieri, {
        "fine_entrate": [990, 1170], "uscita": [1230, 1380], "stop": [0.3, 0.6, 1.0],
        "verso": [1, -1]}),
}


def combinazioni(griglia: dict):
    chiavi = list(griglia)
    for valori in itertools.product(*griglia.values()):
        parametri = {}
        for k, v in zip(chiavi, valori):
            if "," in k:
                parametri.update(dict(zip(k.split(","), v)))
            else:
                parametri[k] = v
        yield parametri


def valida(nome: str, p: dict) -> bool:
    if nome == "momento_o_rientro":
        return p["inizio"] < p["decisione"] < p["uscita"]
    if nome == "rottura_range":
        p["fine_entrate"] = p["a"] + 180
        return p["fine_entrate"] < p["uscita"] and not (p["verso"] == -1 and p["stop"] == "meta")
    if nome == "ora_fissa":
        return p["entrata"] + p["durata"] <= 1380
    return True


# ------------------------------------------------------------------ valutazione

def t_stat(r: np.ndarray) -> float:
    return float(r.mean() / r.std(ddof=1) * np.sqrt(len(r))) if len(r) > 2 and r.std() > 0 else 0.0


def walk_forward(sviluppo: dict):
    """Ogni anno sceglie la combinazione con il t-stat migliore nei 3 anni prima
    (almeno 30 trade) e la usa sull'anno dopo, che non ha visto."""
    anni = sorted({a for t in sviluppo.values() if not t.empty for a in t["anno"].unique()})
    fuori, scelte = [], []
    for anno in anni[ANNI_ALLENAMENTO:]:
        def punti(k):
            t = sviluppo[k]
            if t.empty:
                return -np.inf
            r = t[(t["anno"] >= anno - ANNI_ALLENAMENTO) & (t["anno"] < anno)]["R"].to_numpy()
            return t_stat(r) if len(r) >= 30 else -np.inf
        migliore = max(sviluppo, key=punti)
        t = sviluppo[migliore]
        fuori.append(t[t["anno"] == anno])
        scelte.append({"anno": anno, "parametri": migliore})
    oos = pd.concat(fuori) if fuori else pd.DataFrame(columns=["R", "giorno"])
    return oos, scelte


def valuta_famiglia(m: Mercato, nome: str, funzione, griglia: dict, percorso: pd.DataFrame,
                    max_trade: int = 1):
    prove = {}
    for p in combinazioni(griglia):
        if not valida(nome, p):
            continue
        t = simula_ordini(percorso, funzione(m, **p), max_trade, m.costi)
        if not t.empty:
            t["anno"] = pd.DatetimeIndex(t["giorno"]).year
        prove[json.dumps(p, sort_keys=True)] = t
    sviluppo = {k: t[pd.DatetimeIndex(t["giorno"]) < FINE_SVILUPPO] if not t.empty else t
                for k, t in prove.items()}
    pf_positivi = np.mean([statistiche(t, RISCHIO).get("profit_factor", 0) > 1 for t in sviluppo.values()])

    oos, scelte = walk_forward(sviluppo)
    s = statistiche(oos, RISCHIO)
    anni_oos = per_anno(oos, RISCHIO)
    s.update({
        "t_stat": round(t_stat(oos["R"].to_numpy()), 2) if len(oos) else 0,
        "anni_in_utile": f"{int((anni_oos['R_totale'] > 0).sum())}/{len(anni_oos)}" if len(anni_oos) else "-",
        "griglia_pf_sopra_1_%": round(100 * pf_positivi),
        "combinazioni": len(prove),
    })
    s.update(monte_carlo(oos, RISCHIO))
    passa = (s.get("trade", 0) >= 150 and s.get("profit_factor", 0) >= 1.2 and s["t_stat"] >= 2.5
             and len(anni_oos) and (anni_oos["R_totale"] > 0).mean() >= 0.6 and pf_positivi >= 0.5)
    s["supera_sviluppo"] = bool(passa)
    return s, scelte, prove


def finale(prove: dict, scelte: list) -> dict:
    """Parametri scelti come nel walk-forward (ultimi 3 anni di sviluppo), provati
    una volta sola sui 18 mesi chiusi."""
    def punti(k):
        t = prove[k]
        if t.empty:
            return -np.inf
        g = pd.DatetimeIndex(t["giorno"])
        r = t[(g >= FINE_SVILUPPO - pd.DateOffset(years=3)) & (g < FINE_SVILUPPO)]["R"].to_numpy()
        return t_stat(r) if len(r) >= 30 else -np.inf
    migliore = max(prove, key=punti)
    t = prove[migliore]
    chiuso = t[pd.DatetimeIndex(t["giorno"]) >= FINE_SVILUPPO]
    s = statistiche(chiuso, RISCHIO)
    s["t_stat"] = round(t_stat(chiuso["R"].to_numpy()), 2) if len(chiuso) else 0
    s["parametri"] = migliore
    return s


def apprendimento(tutte: dict) -> dict:
    """Il sistema "che apprende": ogni anno rifa' la scelta tra TUTTE le combinazioni di
    tutte le famiglie, guardando solo il passato, e usa la vincente l'anno dopo."""
    sviluppo = {k: t[pd.DatetimeIndex(t["giorno"]) < FINE_SVILUPPO] if not t.empty else t
                for k, t in tutte.items()}
    oos, scelte = walk_forward(sviluppo)
    s = statistiche(oos, RISCHIO)
    anni_oos = per_anno(oos, RISCHIO)
    s["t_stat"] = round(t_stat(oos["R"].to_numpy()), 2) if len(oos) else 0
    s["anni_in_utile"] = f"{int((anni_oos['R_totale'] > 0).sum())}/{len(anni_oos)}" if len(anni_oos) else "-"
    s.update(monte_carlo(oos, RISCHIO))
    return s, scelte


def gruppi():
    from . import indicatori
    classiche = {n: (f, g, 1) for n, (f, g) in FAMIGLIE.items()}
    nuove = {n: (f, g, indicatori.MAX_TRADE_GIORNO) for n, (f, g) in indicatori.FAMIGLIE.items()}
    return {"classiche": classiche, "indicatori": nuove, "tutte": {**classiche, **nuove}}


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("zip")
    arg.add_argument("--gruppo", choices=["classiche", "indicatori", "tutte"], default="tutte")
    arg.add_argument("--finale", action="store_true", help="apre il cassetto dei 18 mesi")
    a = arg.parse_args()
    m = carica_mercato(a.zip)
    righe = [f"# Ricerca su {m.nome} ({a.gruppo}) - {datetime.now():%d/%m/%Y %H:%M}", "",
             f"Dati {m.m5.index[0]:%d/%m/%Y} - {m.m5.index[-1]:%d/%m/%Y}; sviluppo fino al "
             f"{FINE_SVILUPPO:%d/%m/%Y}. Rischio {RISCHIO:.0%} a trade. Costi: {m.costi}", ""]
    sintesi, tutte = [], {}
    for nome, (funzione, griglia, max_trade) in gruppi()[a.gruppo].items():
        print(f"{m.nome}: {nome}...", flush=True)
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
    righe += ["## Apprendimento: ogni anno sceglie tra tutte le combinazioni", "",
              pd.DataFrame([s]).T.to_markdown(), "", pd.DataFrame(scelte).to_markdown(index=False), ""]
    righe[4:4] = ["## Sintesi", "", pd.DataFrame(sintesi).to_markdown(index=False), ""]
    Path("risultati").mkdir(exist_ok=True)
    file = Path("risultati") / f"ricerca_{m.nome}_{a.gruppo}_{datetime.now():%Y%m%d_%H%M}.md"
    file.write_text("\n".join(righe), encoding="utf-8")
    print("\n".join(righe[:12 + len(sintesi)]))
    print(f"\nRapporto: {file}")


if __name__ == "__main__":
    main()
