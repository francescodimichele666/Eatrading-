# Risultati 22/10/2026: indicatori, forex e coppie opposte

Regole: [2026-10-22_indicatori_e_coppie.md](2026-10-22_indicatori_e_coppie.md).
Rischio 1% a trade, take profit 2,5 volte lo stop, costi veri del conto
(spread mediano delle barre: circa 1,1 pip sui cambi, conto standard senza
commissione; 0,2 pip di slittamento). Dati 07/2017 - 03/2025, walk-forward.
Il cassetto degli ultimi 18 mesi NON e' stato aperto: nessuna famiglia ha superato lo sviluppo.

## Profit factor fuori campione (soglia per i soldi veri: 1,20)

| Famiglia | Oro | EURUSD | USDCHF | AUDUSD | USDCAD |
|---|---|---|---|---|---|
| trend_ema | **1,15** | 0,99 | 0,69 | 0,90 | **1,17** |
| bollinger | 0,95 | 0,99 | 0,78 | 0,99 | 1,05 |
| ichimoku | 0,98 | 0,95 | 0,69 | 0,84 | 0,89 |
| 4 famiglie del 21/10 (migliore) | 1,04 | 0,90 | 0,89 | 0,88 | 0,94 |
| apprendimento (sceglie ogni anno) | 1,06 | 0,73 | 0,88 | 0,88 | 0,75 |

trend_ema su USDCAD: 365 trade, t-stat 1,14, solo il 12% della griglia sopra 1: fortuna di una combinazione.

## Coppie opposte

| Famiglia | EURUSD/USDCHF | AUDUSD/USDCAD |
|---|---|---|
| divergenza del cross (EURCHF, AUDCAD) | 0,65 | 0,92 |
| conferma sulla prima coppia | 0,85 | 0,87 |
| conferma sulla seconda coppia | 0,87 | 1,08 |
| apprendimento | 0,85 | 0,97 |

Il cross sintetico usa apertura e chiusura di ogni barra M5 (il primo tentativo
con massimo x massimo esagerava gli stop ed e' stato scartato).

## Senza costi (mediana della griglia, sviluppo)

| | EURUSD | USDCHF | AUDUSD | USDCAD |
|---|---|---|---|---|
| trend_ema | 1,03 | 1,02 | 1,09 | 1,04 |
| bollinger | 1,04 | 0,94 | 1,09 | 1,10 |
| ichimoku | 1,06 | 1,01 | 1,04 | 0,96 |

Anche gratis, queste strategie guadagnano pochissimo (PF 1,0-1,1). Lo spread
di circa 1 pip su trade da M15/H1 (stop di 5-15 pip) toglie circa 0,2 al
profit factor, quindi tutto diventa negativo.

## Conclusione

Le strategie classiche a indicatori, intraday, sui cambi principali e sull'oro,
non hanno un vantaggio che sopravvive ai costi. Il sistema che "apprende" non
lo crea: sceglie bene solo se tra le candidate ce n'e' una buona.
