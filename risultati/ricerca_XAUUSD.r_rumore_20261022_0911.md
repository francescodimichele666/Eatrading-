# Ricerca su XAUUSD.r (rumore) - 22/10/2026 09:10

Dati 02/07/2017 - 21/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=0.01, commissione_oncia=0.07, spread_minimo_rel=2.1760154738878142e-05, slittamento_rel=2.4177949709864606e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| zona_di_rumore                              |    1417 |            0.89 |     -0.06 |    -1.82 | 1/6             |                      0 |                      74.2 |             16 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1417 |            0.89 |     -0.06 |    -1.82 | 1/6             |                    nan |                      74.2 |            nan |               nan |

## zona_di_rumore

|                         | 0     |
|:------------------------|:------|
| trade                   | 1417  |
| vincenti_%              | 36.6  |
| R_medio                 | -0.06 |
| R_totale                | -85.0 |
| profit_factor           | 0.89  |
| rendimento_%            | -61.7 |
| drawdown_max_%          | 66.9  |
| t_stat                  | -1.82 |
| anni_in_utile           | 1/6   |
| griglia_pf_sopra_1_%    | 0     |
| combinazioni            | 16    |
| drawdown_mediano_%      | 67.5  |
| drawdown_95%_dei_casi_% | 74.2  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                 |
|-------:|:----------------------------------------------------------|
|   2020 | {"inizio": 600, "k": 1.0, "stop": 1.0, "uscita": "rr"}    |
|   2021 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"}    |
|   2022 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "segui"} |
|   2023 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "segui"} |
|   2024 | {"inizio": 990, "k": 1.5, "stop": 0.5, "uscita": "rr"}    |
|   2025 | {"inizio": 990, "k": 1.0, "stop": 1.0, "uscita": "rr"}    |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0     |
|:------------------------|:------|
| trade                   | 1417  |
| vincenti_%              | 36.6  |
| R_medio                 | -0.06 |
| R_totale                | -85.0 |
| profit_factor           | 0.89  |
| rendimento_%            | -61.7 |
| drawdown_max_%          | 66.9  |
| t_stat                  | -1.82 |
| anni_in_utile           | 1/6   |
| drawdown_mediano_%      | 67.5  |
| drawdown_95%_dei_casi_% | 74.2  |

|   anno | parametri                                                                |
|-------:|:-------------------------------------------------------------------------|
|   2020 | zona_di_rumore {"inizio": 600, "k": 1.0, "stop": 1.0, "uscita": "rr"}    |
|   2021 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"}    |
|   2022 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "segui"} |
|   2023 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "segui"} |
|   2024 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 0.5, "uscita": "rr"}    |
|   2025 | zona_di_rumore {"inizio": 990, "k": 1.0, "stop": 1.0, "uscita": "rr"}    |
