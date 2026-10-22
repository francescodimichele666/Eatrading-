# Ricerca su AUDUSD (rumore) - 22/10/2026 09:10

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=0.0001567152483936687, slittamento_rel=2.8493681526121582e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| zona_di_rumore                              |    1272 |            0.88 |    -0.064 |    -1.93 | 1/6             |                      0 |                      71.7 |             16 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1272 |            0.88 |    -0.064 |    -1.93 | 1/6             |                    nan |                      71.7 |            nan |               nan |

## zona_di_rumore

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1272   |
| vincenti_%              | 37.0   |
| R_medio                 | -0.064 |
| R_totale                | -81.9  |
| profit_factor           | 0.88   |
| rendimento_%            | -59.7  |
| drawdown_max_%          | 59.7   |
| t_stat                  | -1.93  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 16     |
| drawdown_mediano_%      | 65.1   |
| drawdown_95%_dei_casi_% | 71.7   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                              |
|-------:|:-------------------------------------------------------|
|   2020 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2023 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1272   |
| vincenti_%              | 37.0   |
| R_medio                 | -0.064 |
| R_totale                | -81.9  |
| profit_factor           | 0.88   |
| rendimento_%            | -59.7  |
| drawdown_max_%          | 59.7   |
| t_stat                  | -1.93  |
| anni_in_utile           | 1/6    |
| drawdown_mediano_%      | 65.1   |
| drawdown_95%_dei_casi_% | 71.7   |

|   anno | parametri                                                             |
|-------:|:----------------------------------------------------------------------|
|   2020 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2021 | zona_di_rumore {"inizio": 600, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2022 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2023 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2024 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
|   2025 | zona_di_rumore {"inizio": 990, "k": 1.5, "stop": 1.0, "uscita": "rr"} |
