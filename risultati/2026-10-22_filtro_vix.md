# Filtro della paura (VIX) e portafoglio - 22/10/2026

Idea, scritta prima del test: la zona di rumore sfrutta chi deve comprare
quando il mercato sale e vendere quando scende per coprire le opzioni. Questa
spinta è più forte quando il mercato è nervoso. Tre filtri decisi prima di
guardare i risultati, sempre con il VIX di ieri (noto prima dell'apertura):

- VIX di ieri sopra la sua mediana dell'ultimo anno;
- VIX di ieri sopra la sua media degli ultimi 5 giorni (paura in salita);
- VIX di ieri sopra 20.

Variante fissa: apertura 09:30, k 1, stop 1, take profit 2,5. Dati VIX
giornalieri da TradingView (CBOE:VIX).

Nota onesta: gli ultimi 18 mesi degli indici li avevo già guardati con la
zona di rumore, quindi non sono un cassetto pulito. Il vero esame è il demo.

| Filtro | S&P sviluppo | S&P ultimi 18 mesi | Nasdaq sviluppo | Nasdaq ultimi 18 mesi |
|---|---|---|---|---|
| nessuno | PF 1,12 (t 2,6) | 1,04 | 1,19 (t 3,5) | 0,98 |
| **VIX sopra la mediana di un anno** | **1,19** (t 2,9) | **1,12** | **1,23** (t 3,1) | **1,12** |
| VIX in salita | 1,07 | 0,92 | 1,11 | 0,95 |
| VIX sopra 20 | 1,22 | 1,00 | 1,15 | 1,16 |

## Portafoglio (rischio 1% per trade, somma semplice, 2019-2026)

| Combinazione | PF giornaliero | Sharpe | Drawdown max | Ultimi 18 mesi |
|---|---|---|---|---|
| zona di rumore S&P + Nasdaq, senza filtro | 1,21-1,22 | 1,2 | 27-35% | da -5% a +10% |
| **zona di rumore S&P + Nasdaq con filtro VIX** | **1,36** | **1,85** | 37% | **+33%** |
| + breakout Nasdaq + idea B oro | 1,17 | 0,95 | 42% | +43% |

Anni della zona S&P + Nasdaq con filtro VIX (rischio 1%): 2019 +26%, 2020 +32%,
2021 +21%, 2022 +93%, 2023 -10%, 2024 +90%, 2025 +46%, 2026 finora 0%.

Aggiungere breakout e oro non migliora: peggiora la regolarità. Il drawdown del
37% con rischio 1% è troppo alto: S&P e Nasdaq si muovono quasi insieme, quindi
il bot usa lo 0,5% per indice (drawdown atteso circa la metà).

## Decisione

Il bot demo usa la zona di rumore su S&P 500 e Nasdaq 100 solo nei giorni con
il VIX sopra la mediana, rischio 0,5% per indice. L'idea B sull'oro resta come
prova separata.
