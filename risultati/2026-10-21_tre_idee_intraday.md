# Tre idee intraday su XAUUSD - 21/10/2026 18:36

Dati 01/01/2015 - 21/10/2026, simulazione su M5. Regole in 2026-10-21_ipotesi_intraday.md.

## Sintesi (walk-forward)

| idea   |   trade |   profit_factor |   R_medio |   drawdown_max_% | anni_in_utile   |   MC_95% | soglia   |
|:-------|--------:|----------------:|----------:|-----------------:|:----------------|---------:|:---------|
| A      |    1428 |            1    |     0.002 |             34.8 | 4/8             |     46   | no       |
| B      |     379 |            1.07 |     0.027 |             10.6 | 5/7             |     20.2 | no       |
| C      |     811 |            1    |    -0     |             27.3 | 5/8             |     26.5 | no       |

## A - rottura del range notturno all'apertura di Londra

Regole base:

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|    1904 |         52.3 |    -0.004 |       -8.3 |            0.99 |           -9.4 |             32.2 |

Regole base senza costi: {'trade': 1904, 'vincenti_%': 52.7, 'R_medio': 0.016, 'R_totale': 29.7, 'profit_factor': 1.04, 'rendimento_%': 20.4, 'drawdown_max_%': 21.3}

Walk-forward (solo anni di prova):

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|    1428 |         39.7 |     0.002 |        2.6 |               1 |           -4.5 |             34.8 |

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2019 |     196 |         35.2 |    -0.036 |       -7.1 |            0.94 |           -6.2 |             16   |
| 2020 |     177 |         36.2 |     0     |        0   |            1    |           -1   |             15   |
| 2021 |     195 |         34.9 |     0.002 |        0.4 |            1    |           -0.9 |             15.2 |
| 2022 |     209 |         32.1 |     0.001 |        0.1 |            1    |           -1.4 |             19.9 |
| 2023 |     197 |         35   |    -0.077 |      -15.2 |            0.86 |          -11.4 |             17   |
| 2024 |     181 |         47.5 |     0.103 |       18.7 |            1.24 |           14.3 |             10.7 |
| 2025 |     162 |         47.5 |    -0.036 |       -5.8 |            0.91 |           -4.6 |              8.4 |
| 2026 |     111 |         60.4 |     0.103 |       11.5 |            1.39 |            8.8 |              2.2 |

Monte Carlo: {'drawdown_mediano_%': 33.7, 'drawdown_95%_dei_casi_%': 46.0}

Parametri scelti:

|   anno | stop    |   target |
|-------:|:--------|---------:|
|   2019 | meta    |      1.5 |
|   2020 | meta    |      1.5 |
|   2021 | meta    |      1.5 |
|   2022 | meta    |      2   |
|   2023 | opposto |      2   |
|   2024 | opposto |      2   |
|   2025 | opposto |      2   |
|   2026 | opposto |      1   |

**Soglia per la demo superata: NO**

## B - momentum all'apertura di New York

Regole base:

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|     394 |         49.5 |     0.034 |       13.6 |            1.12 |            9.9 |              9.2 |

Regole base senza costi: {'trade': 394, 'vincenti_%': 49.7, 'R_medio': 0.049, 'R_totale': 19.4, 'profit_factor': 1.17, 'rendimento_%': 14.8, 'drawdown_max_%': 8.6}

Walk-forward (solo anni di prova):

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|     379 |         45.1 |     0.027 |       10.2 |            1.07 |            6.5 |             10.6 |

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2020 |      15 |         46.7 |     0.19  |        2.9 |            1.49 |            2.1 |              2.5 |
| 2021 |      22 |         36.4 |     0.075 |        1.7 |            1.15 |            1.1 |              5   |
| 2022 |     100 |         47   |     0.007 |        0.7 |            1.02 |            0.2 |              8.4 |
| 2023 |     103 |         47.6 |     0.098 |       10.1 |            1.23 |            7.5 |              6.3 |
| 2024 |      16 |         37.5 |    -0.287 |       -4.6 |            0.5  |           -3.4 |              5.2 |
| 2025 |      96 |         47.9 |     0.018 |        1.7 |            1.07 |            1.1 |              5.2 |
| 2026 |      27 |         29.6 |    -0.084 |       -2.3 |            0.85 |           -1.9 |              8   |

Monte Carlo: {'drawdown_mediano_%': 13.5, 'drawdown_95%_dei_casi_%': 20.2}

Parametri scelti:

|   anno |   soglia |   stop |
|-------:|---------:|-------:|
|   2020 |      0.7 |    0.3 |
|   2021 |      0.7 |    0.3 |
|   2022 |      0.3 |    0.3 |
|   2023 |      0.3 |    0.3 |
|   2024 |      0.7 |    0.3 |
|   2025 |      0.3 |    0.5 |
|   2026 |      0.5 |    0.3 |

**Soglia per la demo superata: NO**

## C - rottura H1 nella direzione del trend giornaliero

Regole base:

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|    1228 |         47.6 |    -0.006 |       -7.4 |            0.99 |           -8.2 |               33 |

Regole base senza costi: {'trade': 1228, 'vincenti_%': 48.3, 'R_medio': 0.012, 'R_totale': 15.1, 'profit_factor': 1.03, 'rendimento_%': 8.7, 'drawdown_max_%': 26.5}

Walk-forward (solo anni di prova):

|   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
|     811 |         48.5 |        -0 |       -0.3 |               1 |             -2 |             27.3 |

|      |   trade |   vincenti_% |   R_medio |   R_totale |   profit_factor |   rendimento_% |   drawdown_max_% |
|-----:|--------:|-------------:|----------:|-----------:|----------------:|---------------:|-----------------:|
| 2019 |      68 |         50   |     0.153 |       10.4 |            1.34 |            7.8 |              4.1 |
| 2020 |      88 |         46.6 |    -0.105 |       -9.2 |            0.79 |           -6.9 |              9.6 |
| 2021 |      84 |         38.1 |    -0.144 |      -12.1 |            0.7  |           -8.9 |             10   |
| 2022 |      93 |         51.6 |     0.002 |        0.2 |            1.01 |            0.1 |              6.6 |
| 2023 |     175 |         45.1 |    -0.078 |      -13.7 |            0.79 |          -10   |             11.5 |
| 2024 |      85 |         49.4 |     0.048 |        4.1 |            1.18 |            3   |              3.3 |
| 2025 |     128 |         57.8 |     0.066 |        8.4 |            1.27 |            6.3 |              4.7 |
| 2026 |      90 |         47.8 |     0.129 |       11.6 |            1.31 |            8.7 |              3.7 |

Monte Carlo: {'drawdown_mediano_%': 18.8, 'drawdown_95%_dei_casi_%': 26.5}

Parametri scelti:

|   anno |   barre |   stop |
|-------:|--------:|-------:|
|   2019 |      40 |    1.5 |
|   2020 |      40 |    1.5 |
|   2021 |      40 |    2   |
|   2022 |      40 |    3   |
|   2023 |      10 |    3   |
|   2024 |      40 |    3   |
|   2025 |      20 |    3   |
|   2026 |      20 |    1.5 |

**Soglia per la demo superata: NO**

## Note

- Lo storico M5 di FP Markets e' completo solo da meta' 2017 (2015-2016 quasi vuoti): gli anni utili sono circa 9.
- Nessuna delle tre idee supera la soglia fissata prima del test.
- La piu' vicina e' B (momentum all'apertura di New York): profit factor 1,12 con regole base e 1,07 nel walk-forward, in utile 5 anni di prova su 7, circa 45 trade l'anno. Troppo poco per rischiare soldi veri.
