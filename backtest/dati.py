"""Lettura dello ZIP prodotto da fase1_esporta_dati.py.

Gli orari di MT5 sono quelli del server del broker. FP Markets, come la
maggior parte dei broker, usa l'ora di New York + 7 ore (la giornata di
trading cambia alle 17:00 di New York). Qui li convertiamo in UTC.
"""

import io
import json
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

ORE_BROKER_SU_NEW_YORK = 7


@dataclass
class Dati:
    oro_m5: pd.DataFrame
    oro_m1: pd.DataFrame | None
    cambi_d1: dict[str, pd.DataFrame]
    fred: dict[str, pd.Series]
    info: dict = field(default_factory=dict)


def ora_broker_a_utc(secondi: pd.Series) -> pd.DatetimeIndex:
    """Converte i secondi "ora broker" di MT5 in orari UTC."""
    ora_ny = pd.to_datetime(secondi, unit="s") - pd.Timedelta(hours=ORE_BROKER_SU_NEW_YORK)
    return pd.DatetimeIndex(ora_ny).tz_localize(
        "America/New_York", ambiguous="NaT", nonexistent="shift_forward"
    ).tz_convert("UTC")


def _barre(archivio: zipfile.ZipFile, nome: str, intraday: bool) -> pd.DataFrame:
    with archivio.open(nome) as f:
        df = pd.read_csv(f, compression="gzip")
    if intraday:
        df.index = ora_broker_a_utc(df["time"])
        df = df[df.index.notna()]
    else:
        # barre giornaliere: conta la data del broker (la barra chiude alle 17:00 di New York)
        df.index = pd.to_datetime(df["time"], unit="s").dt.normalize()
    return df.drop(columns="time").sort_index()


def _fred(archivio: zipfile.ZipFile, nome: str) -> pd.Series:
    with archivio.open(nome) as f:
        df = pd.read_csv(io.TextIOWrapper(f), na_values=".")
    df.columns = ["data", "valore"]
    serie = pd.Series(df["valore"].values, index=pd.to_datetime(df["data"]), name=nome)
    return serie.dropna().astype(float)


def carica(percorso_zip: str | Path) -> Dati:
    with zipfile.ZipFile(percorso_zip) as archivio:
        nomi = archivio.namelist()
        info = json.loads(archivio.read("info.json")) if "info.json" in nomi else {}
        oro = info.get("simbolo_oro", "XAUUSD")
        m5 = _barre(archivio, f"mt5_{oro}_M5.csv.gz", intraday=True)
        nome_m1 = f"mt5_{oro}_M1.csv.gz"
        m1 = _barre(archivio, nome_m1, intraday=True) if nome_m1 in nomi else None
        cambi = {
            n.removeprefix("mt5_").removesuffix("_D1.csv.gz")[:6]: _barre(archivio, n, intraday=False)
            for n in nomi if n.endswith("_D1.csv.gz")
        }
        fred = {
            n.removeprefix("fred_").removesuffix(".csv"): _fred(archivio, n)
            for n in nomi if n.startswith("fred_")
        }
    return Dati(oro_m5=m5, oro_m1=m1, cambi_d1=cambi, fred=fred, info=info)


def controlla_fuso_orario(dati: Dati) -> str:
    """Confronta l'orologio del broker al momento dell'esportazione con UTC."""
    tick, utc = dati.info.get("ultimo_tick_broker"), dati.info.get("ora_utc_al_tick")
    if not tick or not utc:
        return "Fuso orario del broker non verificabile (manca info.json)."
    differenza = round((tick - utc) / 3600)
    atteso = round(
        (pd.Timestamp(utc, unit="s", tz="UTC").tz_convert("America/New_York").utcoffset().total_seconds()
         / 3600) + ORE_BROKER_SU_NEW_YORK
    )
    esito = "OK" if differenza == atteso else "DIVERSO DAL PREVISTO, verificare"
    return f"Orologio broker = UTC{differenza:+d} ore all'esportazione (previsto UTC{atteso:+d}): {esito}"
