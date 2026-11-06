# Ricerca su EURUSD (rumore) - 22/10/2026 09:10

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.786651008025054e-05, slittamento_rel=1.7793910923681917e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| zona_di_rumore                              |    1382 |            0.83 |     -0.09 |    -2.84 | 0/6             |                      0 |                      80.3 |             16 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1382 |            0.83 |     -0.09 |    -2.84 | 0/6             |                    nan |                      80.3 |            nan |               nan |

## zona_di_rumore

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1382   |
| vincenti_%              | 36.6   |
| R_medio                 | -0.09  |
| R_totale                | -124.7 |
| profit_factor           | 0.83   |
| rendimento_%            | -73.9  |
| drawdown_max_%          | 75.6   |
| t_stat                  | -2.84  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 16     |
| drawdown_mediano_%      | 76.6   |
| drawdown_95%_dei_casi_% | 80.3   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                              |
|-------:|:-------------------------------------------------------|
|   2020 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2023 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1382   |
| vincenti_%              | 36.6   |
| R_medio                 | -0.09  |
| R_totale                | -124.7 |
| profit_factor           | 0.83   |
| rendimento_%            | -73.9  |
| drawdown_max_%          | 75.6   |
| t_stat                  | -2.84  |
| anni_in_utile           | 0/6    |
| drawdown_mediano_%      | 76.6   |
| drawdown_95%_dei_casi_% | 80.3   |

|   anno | parametri                                                             |
|-------:|:----------------------------------------------------------------------|
|   2020 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2023 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
