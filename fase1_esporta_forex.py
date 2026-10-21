"""Esporta lo storico M5 dei cambi principali, per cercare strategie anche sul forex.

Per ogni simbolo crea un file logs/forex_<SIMBOLO>.zip (circa 10 MB l'uno) con:
- barre M5 dal 2017 (con lo spread del broker per ogni barra);
- le regole del simbolo (contratto, punto, swap) e lo spread misurato dal vivo per 20 secondi.

Uso: doppio clic su esporta_forex.bat (oppure: python fase1_esporta_forex.py).
"""

import json
import statistics
import sys
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from fase0_controllo import carica_config, collega
from fase1_esporta_dati import barre_csv_gz, trova_cambio

try:
    import MetaTrader5 as mt5
except ImportError:
    print("ERRORE: libreria MetaTrader5 non installata. Esegui esporta_forex.bat.")
    sys.exit(1)

CARTELLA = Path(__file__).resolve().parent
SIMBOLI = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "EURJPY", "GBPJPY",
           "XAGUSD"]
INIZIO = datetime(2017, 1, 1, tzinfo=timezone.utc)


def spread_dal_vivo(simbolo, secondi=20):
    valori = []
    for _ in range(secondi):
        tick = mt5.symbol_info_tick(simbolo)
        if tick and tick.ask > 0 and tick.bid > 0:
            valori.append(tick.ask - tick.bid)
        time.sleep(1)
    return statistics.median(valori) if valori else None


def main():
    if collega(carica_config().get("mt5", {})) is None:
        return 1
    adesso = datetime.now(timezone.utc)
    cartella = CARTELLA / "logs"
    cartella.mkdir(exist_ok=True)
    for nome in SIMBOLI:
        simbolo = trova_cambio(nome)
        if simbolo is None:
            print(f"{nome} non disponibile su questo conto, lo salto.")
            continue
        mt5.symbol_select(simbolo, True)
        print(f"Scarico {simbolo} M5 dal 2017...", flush=True)
        dati, righe = barre_csv_gz(simbolo, mt5.TIMEFRAME_M5, INIZIO, adesso)
        info = mt5.symbol_info(simbolo)
        tick = mt5.symbol_info_tick(simbolo)
        print(f"  {righe} barre. Misuro lo spread per 20 secondi...", flush=True)
        regole = {
            "simbolo": simbolo, "creato_utc": adesso.isoformat(), "barre_m5": righe,
            "cifre": info.digits, "punto": info.point, "contratto": info.trade_contract_size,
            "valuta_profitto": info.currency_profit, "lotto_minimo": info.volume_min,
            "swap_long": info.swap_long, "swap_short": info.swap_short,
            "spread_vivo": spread_dal_vivo(simbolo), "prezzo": tick.bid if tick else None,
            "ultimo_tick_broker": int(tick.time) if tick else None,
            "ora_utc_al_tick": int(time.time()),
        }
        file = cartella / f"forex_{nome}.zip"
        with zipfile.ZipFile(file, "w", zipfile.ZIP_STORED) as archivio:
            archivio.writestr(f"mt5_{simbolo}_M5.csv.gz", dati)
            archivio.writestr("regole.json", json.dumps(regole, indent=2))
        print(f"  creato {file.name} ({file.stat().st_size / 1_000_000:.1f} MB)")
    mt5.shutdown()
    print("\nFatto. Manda a Claude tutti i file forex_*.zip della cartella logs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
