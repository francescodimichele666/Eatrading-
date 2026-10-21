"""Fase 1: esporta lo storico necessario per il backtest in un unico file ZIP.

Cosa scarica:
- dal tuo MT5: barre M5 dell'oro dal 2015 e barre M1 degli ultimi 3 anni,
  con lo spread reale del broker per ogni barra;
- dal tuo MT5: barre giornaliere dei 6 cambi che compongono il DXY;
- da FRED (Federal Reserve): tassi USA, tassi reali e indice del dollaro.

Alla fine crea logs/dati_backtest_<data>.zip: e' il file da mandare a Claude.

Uso: doppio clic su esporta_dati.bat (oppure: python fase1_esporta_dati.py).
"""

import csv
import gzip
import io
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import requests

from fase0_controllo import carica_config, collega, trova_simbolo

try:
    import MetaTrader5 as mt5
except ImportError:
    print("ERRORE: libreria MetaTrader5 non installata. Esegui esporta_dati.bat.")
    sys.exit(1)

CARTELLA = Path(__file__).resolve().parent
ANNO_INIZIO_M5 = 2015
ANNI_M1 = 3
CAMBI_DXY = ["EURUSD", "USDJPY", "GBPUSD", "USDCAD", "USDSEK", "USDCHF"]
SERIE_FRED = {
    "DFII10": "tasso reale USA 10 anni",
    "DGS10": "rendimento Treasury 10 anni",
    "DGS2": "rendimento Treasury 2 anni",
    "T10YIE": "inflazione attesa 10 anni",
    "DTWEXBGS": "indice del dollaro (Fed, ampio)",
}


def trova_cambio(nome):
    if mt5.symbol_info(nome) is not None:
        return nome
    for s in mt5.symbols_get(f"{nome}*") or []:
        return s.name
    return None


def barre_csv_gz(simbolo, timeframe, inizio, fine):
    """Scarica le barre mese per mese (MT5 ne restituisce un numero limitato
    per chiamata) e le restituisce come CSV compresso."""
    mt5.symbol_select(simbolo, True)
    buffer = io.StringIO()
    scrittore = csv.writer(buffer)
    scrittore.writerow(["time", "open", "high", "low", "close", "tick_volume", "spread"])
    righe = 0
    ultimo_tempo = 0
    anno, mese = inizio.year, inizio.month
    while datetime(anno, mese, 1, tzinfo=timezone.utc) < fine:
        da = datetime(anno, mese, 1, tzinfo=timezone.utc)
        anno, mese = (anno + 1, 1) if mese == 12 else (anno, mese + 1)
        a = min(datetime(anno, mese, 1, tzinfo=timezone.utc), fine)
        barre = mt5.copy_rates_range(simbolo, timeframe, da, a)
        if barre is None:
            continue
        for b in barre:
            if b["time"] <= ultimo_tempo:
                continue
            ultimo_tempo = int(b["time"])
            scrittore.writerow([ultimo_tempo, b["open"], b["high"], b["low"], b["close"],
                                int(b["tick_volume"]), int(b["spread"])])
            righe += 1
    return gzip.compress(buffer.getvalue().encode()), righe


def scarica_fred(serie):
    risposta = requests.get(
        "https://fred.stlouisfed.org/graph/fredgraph.csv",
        params={"id": serie},
        timeout=60,
    )
    risposta.raise_for_status()
    return risposta.content


def main():
    cfg = carica_config()
    conto = collega(cfg.get("mt5", {}))
    if conto is None:
        return 1
    oro = trova_simbolo(cfg.get("controllo", {}).get("simbolo", "XAUUSD"))
    if oro is None:
        print("ERRORE: nessun simbolo dell'oro trovato.")
        return 1

    adesso = datetime.now(timezone.utc)
    tick = mt5.symbol_info_tick(oro)
    info = {
        "creato_utc": adesso.isoformat(),
        "broker": conto.company,
        "server": conto.server,
        "simbolo_oro": oro,
        # differenza tra l'orologio del broker e UTC, per convertire gli orari
        "ultimo_tick_broker": int(tick.time) if tick else None,
        "ora_utc_al_tick": int(adesso.timestamp()),
        "file": {},
    }

    nome_zip = CARTELLA / "logs" / f"dati_backtest_{adesso:%Y%m%d}.zip"
    nome_zip.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(nome_zip, "w", zipfile.ZIP_STORED) as archivio:
        lavori = [
            (oro, mt5.TIMEFRAME_M5, datetime(ANNO_INIZIO_M5, 1, 1, tzinfo=timezone.utc), "M5"),
            (oro, mt5.TIMEFRAME_M1, datetime(adesso.year - ANNI_M1, 1, 1, tzinfo=timezone.utc), "M1"),
        ]
        for cambio in CAMBI_DXY:
            trovato = trova_cambio(cambio)
            if trovato is None:
                print(f"Attenzione: {cambio} non disponibile su questo conto, lo salto.")
                continue
            lavori.append((trovato, mt5.TIMEFRAME_D1,
                           datetime(ANNO_INIZIO_M5, 1, 1, tzinfo=timezone.utc), "D1"))

        for simbolo, timeframe, inizio, etichetta in lavori:
            print(f"Scarico {simbolo} {etichetta} dal {inizio:%Y}...", flush=True)
            dati, righe = barre_csv_gz(simbolo, timeframe, inizio, adesso)
            nome = f"mt5_{simbolo}_{etichetta}.csv.gz"
            archivio.writestr(nome, dati)
            info["file"][nome] = righe
            print(f"  {righe} barre")
            if righe == 0:
                print("  Nessuna barra: in MT5 apri un grafico di questo simbolo e riprova.")

        for serie, descrizione in SERIE_FRED.items():
            print(f"Scarico da FRED {serie} ({descrizione})...", flush=True)
            try:
                archivio.writestr(f"fred_{serie}.csv", scarica_fred(serie))
                info["file"][f"fred_{serie}.csv"] = "ok"
            except requests.RequestException as errore:
                print(f"  ERRORE: {errore}")
                info["file"][f"fred_{serie}.csv"] = f"errore: {errore}"

        archivio.writestr("info.json", json.dumps(info, indent=2))

    mt5.shutdown()
    dimensione = nome_zip.stat().st_size / 1_000_000
    print(f"\nFatto. File creato: {nome_zip} ({dimensione:.1f} MB)")
    print("Manda questo file a Claude.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
