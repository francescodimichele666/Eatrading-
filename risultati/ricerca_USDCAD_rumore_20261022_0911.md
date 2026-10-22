# Ricerca su USDCAD (rumore) - 22/10/2026 09:10

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.272666319536083e-05, slittamento_rel=1.4265640491593972e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| zona_di_rumore                              |    1215 |            0.93 |    -0.037 |    -1.11 | 2/6             |                      0 |                      61.8 |             16 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1215 |            0.93 |    -0.037 |    -1.11 | 2/6             |                    nan |                      61.8 |            nan |               nan |

## zona_di_rumore

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1215   |
| vincenti_%              | 39.0   |
| R_medio                 | -0.037 |
| R_totale                | -45.2  |
| profit_factor           | 0.93   |
| rendimento_%            | -41.4  |
| drawdown_max_%          | 42.6   |
| t_stat                  | -1.11  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 16     |
| drawdown_mediano_%      | 52.1   |
| drawdown_95%_dei_casi_% | 61.8   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                              |
|-------:|:-------------------------------------------------------|
|   2020 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | {"inizio": 990, "k": 1.0, "stop": 1.0, "uscita": "rr"} |
|   2023 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1215   |
| vincenti_%              | 39.0   |
| R_medio                 | -0.037 |
| R_totale                | -45.2  |
| profit_factor           | 0.93   |
| rendimento_%            | -41.4  |
| drawdown_max_%          | 42.6   |
| t_stat                  | -1.11  |
| anni_in_utile           | 2/6    |
| drawdown_mediano_%      | 52.1   |
| drawdown_95%_dei_casi_% | 61.8   |

|   anno | parametri                                                             |
|-------:|:----------------------------------------------------------------------|
|   2020 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | zona_di_rumore {"inizio": 990, "k": 1.0, "stop": 1.0, "uscita": "rr"} |
|   2023 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
