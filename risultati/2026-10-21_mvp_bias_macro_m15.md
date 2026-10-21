# Backtest MVP XAUUSD - 21/10/2026 18:30

- Dati: 01/01/2015 - 21/10/2026, simulazione su M5
- Orologio broker = UTC+3 ore all'esportazione (previsto UTC+3): OK
- Spread mediano nei dati: 0.04 $
- Giorni con bias long / short / fermo: 898 / 975 / 1209

## Regole base, con bias macro

|    |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|---:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|  0 |    3137 |         41.6 |     -0.07 |       -219 |            0.88 |          -82.7 |             87.8 |

Per anno:

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2016 |     106 |         45.3 |     0.048 |        5.1 |            1.12 |            3.6 |              6.8 |
| 2017 |     218 |         49.5 |     0.106 |       23.1 |            1.21 |           18   |             11.7 |
| 2018 |     256 |         41   |    -0.091 |      -23.3 |            0.85 |          -16.8 |             21.9 |
| 2019 |     207 |         35.3 |    -0.238 |      -49.2 |            0.65 |          -31.4 |             31.4 |
| 2020 |     286 |         40.6 |    -0.091 |      -26   |            0.85 |          -18.6 |             25   |
| 2021 |     312 |         40.7 |    -0.094 |      -29.3 |            0.85 |          -20.6 |             26.5 |
| 2022 |     360 |         44.7 |     0.01  |        3.6 |            1.02 |            1.4 |             15.3 |
| 2023 |     423 |         40.7 |    -0.109 |      -46   |            0.82 |          -30.3 |             35   |
| 2024 |     402 |         45.5 |     0.025 |       10.2 |            1.05 |            6.4 |             14.2 |
| 2025 |     301 |         33.9 |    -0.231 |      -69.4 |            0.65 |          -41.2 |             45.3 |
| 2026 |     266 |         41   |    -0.067 |      -17.8 |            0.88 |          -13.3 |             20.6 |

Monte Carlo: {'drawdown_mediano_%': 84.3, 'drawdown_95%_dei_casi_%': 86.8}

## Regole base, SENZA bias macro (confronto)

|    |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|---:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|  0 |    6159 |         41.6 |    -0.068 |     -421.1 |            0.88 |          -96.6 |             97.1 |

Per anno:

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2016 |     247 |         37.2 |    -0.194 |      -48   |            0.63 |          -30.7 |             34   |
| 2017 |     434 |         42.9 |    -0.05  |      -21.9 |            0.91 |          -16.4 |             17.5 |
| 2018 |     608 |         42.3 |    -0.072 |      -44   |            0.88 |          -29.7 |             32.3 |
| 2019 |     636 |         43.2 |    -0.051 |      -32.2 |            0.92 |          -23.3 |             29.2 |
| 2020 |     614 |         40.6 |    -0.09  |      -55.4 |            0.85 |          -35.4 |             37   |
| 2021 |     631 |         41.8 |    -0.062 |      -39.4 |            0.9  |          -27.3 |             33.9 |
| 2022 |     654 |         44   |    -0.002 |       -1.5 |            1    |           -3.5 |             17.6 |
| 2023 |     619 |         40.1 |    -0.105 |      -65.3 |            0.83 |          -40.1 |             42.7 |
| 2024 |     626 |         42.7 |    -0.04  |      -24.8 |            0.93 |          -18.9 |             31.4 |
| 2025 |     595 |         38.5 |    -0.126 |      -75   |            0.8  |          -44.2 |             48.3 |
| 2026 |     495 |         42.4 |    -0.028 |      -13.6 |            0.95 |          -11.3 |             23.2 |

Monte Carlo: {'drawdown_mediano_%': 96.9, 'drawdown_95%_dei_casi_%': 97.5}

## Walk-forward (solo anni mai visti in ottimizzazione)

|    |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|---:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|  0 |    2392 |         34.8 |     -0.11 |     -262.6 |            0.84 |          -87.6 |             88.9 |

Per anno:

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2019 |     203 |         30.5 |    -0.16  |      -32.6 |            0.78 |          -22.5 |             25.6 |
| 2020 |     265 |         32.5 |    -0.1   |      -26.5 |            0.85 |          -19.1 |             28.8 |
| 2021 |     263 |         39.5 |    -0.071 |      -18.7 |            0.88 |          -14   |             23.3 |
| 2022 |     292 |         41.4 |    -0.039 |      -11.3 |            0.93 |           -9.1 |             14.3 |
| 2023 |     394 |         22.6 |    -0.219 |      -86.3 |            0.73 |          -49.1 |             50   |
| 2024 |     416 |         34.4 |    -0.028 |      -11.7 |            0.96 |          -10.5 |             32   |
| 2025 |     298 |         26.8 |    -0.239 |      -71.3 |            0.68 |          -42.3 |             47.6 |
| 2026 |     261 |         56.3 |    -0.017 |       -4.3 |            0.96 |           -3.7 |             13   |

Monte Carlo: {'drawdown_mediano_%': 88.6, 'drawdown_95%_dei_casi_%': 90.2}

Parametri scelti ogni anno:

|   anno |   tolleranza_atr |   stop_atr |   target_atr |   R_allenamento |
|-------:|-----------------:|-----------:|-------------:|----------------:|
|   2019 |             0.5  |        1.5 |          3   |            17.9 |
|   2020 |             0.5  |        1.5 |          3   |           -19.7 |
|   2021 |             0    |        2   |          3   |           -37.4 |
|   2022 |             0    |        2   |          3   |           -51.1 |
|   2023 |             0.25 |        1   |          3   |            -7.4 |
|   2024 |             0.25 |        1   |          2   |           -44.9 |
|   2025 |             0    |        1   |          2   |           -23.9 |
|   2026 |             0    |        2   |          1.5 |           -76.1 |

## Note sui dati e verifiche aggiuntive

- FRED era in manutenzione durante l'esportazione: la serie DFII10 (2014-06-02 - 2026-10-19) e' stata presa da TradingView (simbolo FRED:DFII10), stessa fonte.
- Lo spread nelle barre MT5 e' spesso 0 negli anni vecchi: il motore usa come minimo 0,09 $ a 4136 $ (misurato dal vivo il 21/10/2026), in proporzione al prezzo, piu' 0,10 $ di slittamento in proporzione e 0,07 $/oncia di commissione.
- Senza alcun costo la strategia fa comunque -0,016 R a trade (profit factor 0,97): non c'e' vantaggio da proteggere.
- Movimento medio dell'oro dalle 9 alle 21 (ora italiana) secondo il bias: short +0,029%, fermo -0,032%, long +0,017%. Il bias macro giornaliero non prevede la direzione intraday.
- Simulazione su M1 (2023-2026) praticamente identica a quella su M5 (-0,085 R contro -0,088 R): il risultato non dipende dalla precisione delle barre.

## Conclusione

Ipotesi MVP respinta: niente Fase 2 con queste regole.
