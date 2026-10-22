"""Filtro della paura per la zona di rumore: si opera solo se la chiusura del VIX di ieri
e' sopra la sua mediana dell'ultimo anno (circa 252 giornate).

Perche': la zona di rumore sfrutta chi compra quando il mercato sale e vende quando scende
per coprire le opzioni; questa spinta e' piu' forte quando il mercato e' nervoso.
Prova: risultati/2026-10-22_filtro_vix.md.

Dati: storico ufficiale del VIX pubblicato dal CBOE (gratuito), salvato in logs/vix.csv
e aggiornato una volta al giorno.
"""

import io
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd
import requests

URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
GIORNATE = 252


def storico(cartella_log: Path) -> pd.Series:
    """Chiusure giornaliere del VIX (indice = data). Scarica al massimo una volta al giorno."""
    file = cartella_log / "vix.csv"
    oggi = datetime.now(timezone.utc).date()
    if not file.exists() or date.fromtimestamp(file.stat().st_mtime) < oggi:
        risposta = requests.get(URL, timeout=30)
        risposta.raise_for_status()
        file.write_text(risposta.text, encoding="utf-8")
    df = pd.read_csv(io.StringIO(file.read_text(encoding="utf-8")))
    df.columns = [c.strip().upper() for c in df.columns]
    return pd.Series(df["CLOSE"].astype(float).to_numpy(),
                     index=pd.to_datetime(df["DATE"], format="%m/%d/%Y")).sort_index()


def giorni_nervosi(vix: pd.Series) -> pd.Series:
    """True nei giorni in cui la chiusura di IERI e' sopra la mediana dell'anno prima."""
    ieri = vix.shift(1)
    return ieri > vix.rolling(GIORNATE, min_periods=200).median().shift(1)


def oggi_si_opera(cartella_log: Path, oggi: date) -> tuple[bool | None, str]:
    """(True/False, spiegazione); None se il dato non c'e' (il bot opera senza filtro)."""
    try:
        vix = storico(cartella_log)
    except (requests.RequestException, OSError, ValueError, KeyError) as errore:
        return None, f"VIX non disponibile ({errore}): opero senza filtro"
    vix = vix[vix.index < pd.Timestamp(oggi)]
    if len(vix) < 200:
        return None, "storico VIX troppo corto: opero senza filtro"
    mediana = float(vix.iloc[-GIORNATE:].median())
    ieri = float(vix.iloc[-1])
    if ieri > mediana:
        return True, f"VIX di ieri {ieri:.1f} sopra la mediana {mediana:.1f}: mercato nervoso, si opera"
    return False, f"VIX di ieri {ieri:.1f} sotto la mediana {mediana:.1f}: mercato calmo, oggi niente trade"
