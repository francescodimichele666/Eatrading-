"""Esegue il backtest completo e scrive un rapporto in risultati/.

Uso: python -m backtest.esegui logs/dati_backtest_AAAAMMGG.zip [--m1]
  --m1  usa le barre M1 (piu' precise, ma solo ultimi 3 anni) per simulare i trade
"""

import argparse
import itertools
from dataclasses import replace
from datetime import datetime
from pathlib import Path

import pandas as pd

from .dati import carica, controlla_fuso_orario
from .motore import Costi, monte_carlo, per_anno, simula, statistiche
from .strategia import Parametri, bias_giornaliero, dxy_sintetico, segnali

GRIGLIA = {
    "tolleranza_atr": [0.0, 0.25, 0.5],
    "stop_atr": [1.0, 1.5, 2.0],
    "target_atr": [1.5, 2.0, 3.0],
}
ANNI_ALLENAMENTO = 3
MIN_TRADE_ALLENAMENTO = 30


def tabella(df: pd.DataFrame) -> str:
    return df.to_markdown() if not df.empty else "(nessun trade)"


def walk_forward(percorso, m5, bias, base: Parametri, costi: Costi):
    """Per ogni anno sceglie i parametri migliori sui 3 anni precedenti
    e li applica all'anno dopo, che non ha mai visto."""
    combinazioni = [replace(base, **dict(zip(GRIGLIA, valori)))
                    for valori in itertools.product(*GRIGLIA.values())]
    tutti = {}
    for p in combinazioni:
        t = simula(percorso, segnali(m5, bias, p), p, costi)
        if not t.empty:
            t["anno"] = pd.DatetimeIndex(t["giorno"]).year
        tutti[p] = t
    anni = sorted({a for t in tutti.values() if not t.empty for a in t["anno"].unique()})
    fuori_campione, scelte = [], []
    for anno in anni[ANNI_ALLENAMENTO:]:
        def punteggio(p):
            t = tutti[p]
            if t.empty:
                return float("-inf")
            allen = t[(t["anno"] >= anno - ANNI_ALLENAMENTO) & (t["anno"] < anno)]
            return allen["R"].sum() if len(allen) >= MIN_TRADE_ALLENAMENTO else float("-inf")
        migliore = max(combinazioni, key=punteggio)
        t = tutti[migliore]
        fuori_campione.append(t[t["anno"] == anno])
        scelte.append({"anno": anno, **{k: getattr(migliore, k) for k in GRIGLIA},
                       "R_allenamento": round(punteggio(migliore), 1)})
    oos = pd.concat(fuori_campione) if fuori_campione else pd.DataFrame()
    return oos, pd.DataFrame(scelte)


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("zip")
    arg.add_argument("--m1", action="store_true")
    arg.add_argument("--senza-walk-forward", action="store_true")
    a = arg.parse_args()

    dati = carica(a.zip)
    m5 = dati.oro_m5
    percorso = dati.oro_m1 if a.m1 and dati.oro_m1 is not None else m5
    if percorso is not m5:
        m5 = m5[m5.index >= percorso.index[0]]
    costi = Costi()
    base = Parametri()

    giorni = pd.DatetimeIndex(sorted(set(m5.index.tz_convert("Europe/Rome").tz_localize(None).normalize())))
    dollaro = dxy_sintetico(dati.cambi_d1)
    if dollaro is None:
        dollaro = dati.fred["DTWEXBGS"]
    bias = bias_giornaliero(giorni, dati.fred["DFII10"], dollaro, base)

    righe = [f"# Backtest MVP XAUUSD - {datetime.now():%d/%m/%Y %H:%M}", "",
             f"- Dati: {m5.index[0]:%d/%m/%Y} - {m5.index[-1]:%d/%m/%Y}, simulazione su "
             f"{'M1' if percorso is not m5 else 'M5'}",
             f"- {controlla_fuso_orario(dati)}",
             f"- Spread mediano nei dati: {percorso['spread'].median() * costi.punto:.2f} $",
             f"- Giorni con bias long / short / fermo: {(bias == 1).sum()} / {(bias == -1).sum()} / {(bias == 0).sum()}",
             ""]

    for titolo, p in [("Regole base, con bias macro", base),
                      ("Regole base, SENZA bias macro (confronto)", replace(base, usa_bias=False))]:
        t = simula(percorso, segnali(m5, bias, p), p, costi)
        righe += [f"## {titolo}", "", tabella(pd.DataFrame([statistiche(t)])), "",
                  "Per anno:", "", tabella(per_anno(t)), "",
                  f"Monte Carlo: {monte_carlo(t)}", ""]

    if not a.senza_walk_forward:
        oos, scelte = walk_forward(percorso, m5, bias, base, costi)
        righe += ["## Walk-forward (solo anni mai visti in ottimizzazione)", "",
                  tabella(pd.DataFrame([statistiche(oos)])), "",
                  "Per anno:", "", tabella(per_anno(oos)), "",
                  f"Monte Carlo: {monte_carlo(oos)}", "",
                  "Parametri scelti ogni anno:", "", tabella(scelte.set_index("anno") if not scelte.empty else scelte), ""]

    cartella = Path("risultati")
    cartella.mkdir(exist_ok=True)
    file = cartella / f"backtest_{datetime.now():%Y%m%d_%H%M}{'_m1' if a.m1 else ''}.md"
    file.write_text("\n".join(righe), encoding="utf-8")
    print("\n".join(righe))
    print(f"\nRapporto: {file}")


if __name__ == "__main__":
    main()
