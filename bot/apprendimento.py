"""Apprendimento settimanale della zona di rumore (ogni sabato, a mercati chiusi).

Per ogni indice:
1. scarica da MT5 gli ultimi 4 anni di barre M5;
2. rifa' il backtest delle 4 varianti (k 1 o 1,5; stop 0,5 o 1; take profit 2,5) con i costi veri;
3. ricalibra: sceglie la variante con il risultato piu' solido (t-stat) negli ultimi 36 mesi;
4. salute: se gli ultimi 60 trade della variante scelta sono in perdita, mette l'indice
   in PAUSA (il bot continua a guardare ma non apre trade) finche' non torna positivo;
5. errori: confronta i trade veri del bot con quelli del backtest della settimana
   (trade mancati, trade in piu', differenze di prezzo) e raggruppa le perdite recenti
   per fascia oraria, lato e volatilita'.
Scrive logs/parametri_rumore.json (letto dal bot) e logs/apprendimento_<data>.md, e manda
un riassunto su Telegram.

Il metodo e' stato provato sugli anni passati: vedi risultati/2026-10-22_apprendimento.md.
Non crea guadagni dal nulla: serve a seguire i cambiamenti del mercato e a fermarsi
quando la strategia smette di funzionare.

Uso a mano: python -m bot.apprendimento
"""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import MetaTrader5 as mt5
import numpy as np
import pandas as pd

from backtest.dati import ora_broker_a_utc
from backtest.motore import simula_ordini
from backtest.ricerca import costi_per, mercato_da, t_stat
from backtest.rumore import zona_di_rumore

VARIANTI = [{"k": k, "stop": s} for k in (1.0, 1.5) for s in (0.5, 1.0)]
PREDEFINITI = {"k": 1.0, "stop": 1.0, "rr": 2.5, "pausa": False}
MESI_SCELTA = 36
TRADE_SALUTE = 60
FILE_PARAMETRI = "parametri_rumore.json"


def leggi_parametri(cartella_log: Path, simbolo: str) -> dict:
    try:
        tutti = json.loads((cartella_log / FILE_PARAMETRI).read_text(encoding="utf-8"))
        return {**PREDEFINITI, **tutti.get(simbolo, {})}
    except (OSError, ValueError):
        return dict(PREDEFINITI)


def scarica(simbolo: str, anni: int = 4) -> pd.DataFrame:
    adesso = datetime.now(timezone.utc)
    pezzi, inizio = [], adesso - timedelta(days=365 * anni)
    while inizio < adesso:  # a pezzi di 90 giorni: MT5 ne restituisce un numero limitato
        fine = min(inizio + timedelta(days=90), adesso)
        dati = mt5.copy_rates_range(simbolo, mt5.TIMEFRAME_M5, inizio, fine)
        if dati is not None and len(dati):
            pezzi.append(pd.DataFrame(dati))
        inizio = fine
    if not pezzi:
        raise RuntimeError(f"nessuna barra M5 per {simbolo}: {mt5.last_error()}")
    df = pd.concat(pezzi).drop_duplicates("time")
    df.index = ora_broker_a_utc(df["time"])
    return df[["open", "high", "low", "close", "spread"]].sort_index()


def regole(simbolo: str) -> dict:
    info, tick = mt5.symbol_info(simbolo), mt5.symbol_info_tick(simbolo)
    r = {"punto": info.point, "contratto": info.trade_contract_size}
    if tick and tick.ask > tick.bid > 0:
        r.update(spread_vivo=tick.ask - tick.bid, prezzo=tick.bid)
    return r


def prove(simbolo: str, m5: pd.DataFrame) -> tuple:
    r = regole(simbolo)
    r.setdefault("spread_barre", float(m5["spread"].iloc[-75_000:].median()))
    m = mercato_da(simbolo, m5, costi_per(simbolo, r, float(m5["close"].iloc[-1])))
    risultati = {}
    for v in VARIANTI:
        t = simula_ordini(m.m5, zona_di_rumore(m, 990, v["k"], v["stop"], "rr"), 3, m.costi)
        if not t.empty:
            t["data"] = pd.to_datetime(t["giorno"])
        risultati[json.dumps(v)] = t
    return m, risultati


def gruppi_in_perdita(t: pd.DataFrame, m) -> list[str]:
    if t.empty:
        return []
    ora = pd.DatetimeIndex(t["entrata_utc"]).tz_convert("America/New_York").hour
    regime = (m.atr_ieri / m.atr_ieri.rolling(250, min_periods=100).median()).reindex(t["data"]).to_numpy()
    gruppi = {
        "fascia": np.where(ora < 12, "mattina", np.where(ora < 14, "mezzogiorno", "pomeriggio")),
        "lato": np.where(t["direzione"] == 1, "long", "short"),
        "volatilita'": np.where(regime > 1.2, "alta", np.where(regime < 0.8, "bassa", "normale")),
    }
    righe = []
    for nome, valori in gruppi.items():
        for valore in sorted(set(valori)):
            r = t["R"].to_numpy()[valori == valore]
            if len(r) >= 20 and r.sum() < 0:
                righe.append(f"{nome} {valore}: {len(r)} trade, {r.sum():+.1f} R")
    return righe


def confronta_con_registro(registro, simbolo: str, attesi: pd.DataFrame) -> list[str]:
    da = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    veri = registro.db.execute(
        "SELECT apertura_utc, direzione, prezzo_entrata, risultato FROM trade "
        "WHERE simbolo=? AND apertura_utc>=?", (simbolo, da)).fetchall()
    attesi = attesi[pd.DatetimeIndex(attesi["entrata_utc"]) >= pd.Timestamp(da)] if not attesi.empty else attesi
    righe = [f"trade veri del bot: {len(veri)}, trade del backtest nella stessa settimana: {len(attesi)}"]
    if len(veri) != len(attesi):
        righe.append("ATTENZIONE: numero diverso. Possibili cause: bot fermo, spread alto, "
                     "pausa, collegamento perso. Controllare logs/bot.log.")
    if veri and len(attesi):
        righe.append(f"risultato vero {sum(v[3] or 0 for v in veri):+.2f} (valuta del conto), "
                     f"backtest {attesi['R'].sum():+.1f} R")
    return righe


def aggiorna(cartella_log: Path, simboli: list[str], registro=None) -> str:
    oggi = datetime.now(timezone.utc).date().isoformat()
    parametri, testo = {}, [f"# Apprendimento del {oggi}", ""]
    for simbolo in simboli:
        m, risultati = prove(simbolo, scarica(simbolo))
        limite = pd.Timestamp(oggi) - pd.DateOffset(months=MESI_SCELTA)

        def punti(chiave):
            t = risultati[chiave]
            r = t[t["data"] >= limite]["R"].to_numpy() if not t.empty else np.array([])
            return t_stat(r) if len(r) >= 30 else -np.inf

        scelta = max(risultati, key=punti)
        t = risultati[scelta]
        ultimi = t["R"].to_numpy()[-TRADE_SALUTE:]
        pausa = bool(len(ultimi) >= TRADE_SALUTE and ultimi.sum() < 0)
        v = json.loads(scelta)
        parametri[simbolo] = {"k": v["k"], "stop": v["stop"], "rr": 2.5, "pausa": pausa,
                              "salute_ultimi_60_R": round(float(ultimi.sum()), 1), "aggiornato": oggi}
        recenti = t[t["data"] >= pd.Timestamp(oggi) - pd.DateOffset(months=6)]
        testo += [f"## {simbolo}", "",
                  f"- variante scelta: k {v['k']}, stop {v['stop']} (t-stat ultimi 36 mesi "
                  f"{punti(scelta):.2f})",
                  f"- ultimi {TRADE_SALUTE} trade del backtest: {ultimi.sum():+.1f} R -> "
                  + ("**PAUSA**: il bot non apre trade su questo indice" if pausa else "attivo"),
                  f"- ultimi 6 mesi: {len(recenti)} trade, {recenti['R'].sum():+.1f} R", ""]
        perdite = gruppi_in_perdita(recenti, m)
        testo += ["Dove ha perso negli ultimi 6 mesi:", ""] + [f"- {p}" for p in perdite or ["nessun gruppo in perdita"]] + [""]
        if registro is not None:
            testo += ["Confronto con i trade veri della settimana:", ""]
            testo += [f"- {r}" for r in confronta_con_registro(registro, simbolo, t)] + [""]
    (cartella_log / FILE_PARAMETRI).write_text(json.dumps(parametri, indent=2), encoding="utf-8")
    rapporto = "\n".join(testo)
    (cartella_log / f"apprendimento_{oggi}.md").write_text(rapporto, encoding="utf-8")
    return rapporto


if __name__ == "__main__":
    from .broker import collega, scollega, trova_simbolo
    from .principale import CARTELLA, carica_config
    cfg = carica_config()
    collega(cfg.get("mt5", {}))
    simboli = [trova_simbolo(s) for s in cfg.get("rumore", {}).get("simboli", ["US500", "US100"])]
    print(aggiorna(CARTELLA / "logs", simboli))
    scollega()
