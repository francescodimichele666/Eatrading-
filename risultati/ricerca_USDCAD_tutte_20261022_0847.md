# Ricerca su USDCAD (tutte) - 22/10/2026 08:44

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.272666319536083e-05, slittamento_rel=1.4265640491593972e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| momento_o_rientro                           |     260 |            0.64 |    -0.105 |    -2.83 | 1/6             |                     14 |                      28.7 |            324 |                 0 |
| rottura_range                               |    1300 |            0.85 |    -0.077 |    -2.29 | 1/6             |                      0 |                      75.9 |             72 |                 0 |
| ora_fissa                                   |    1360 |            0.81 |    -0.029 |    -2.94 | 0/6             |                      0 |                      38.2 |             60 |                 0 |
| massimo_ieri                                |     912 |            0.94 |    -0.018 |    -0.76 | 1/6             |                      0 |                      34.9 |             24 |                 0 |
| trend_ema                                   |     365 |            1.17 |     0.044 |     1.14 | 4/6             |                     12 |                      15.1 |             24 |                 0 |
| bollinger                                   |     486 |            1.05 |     0.022 |     0.44 | 3/6             |                     19 |                      30.1 |             48 |                 0 |
| ichimoku                                    |     565 |            0.89 |    -0.056 |    -1.12 | 2/6             |                      0 |                      47.9 |             24 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     430 |            0.75 |    -0.098 |    -2.38 | 0/6             |                    nan |                      43.2 |            nan |               nan |

## momento_o_rientro

|                         | 0      |
|:------------------------|:-------|
| trade                   | 260    |
| vincenti_%              | 42.3   |
| R_medio                 | -0.105 |
| R_totale                | -27.3  |
| profit_factor           | 0.64   |
| rendimento_%            | -24.3  |
| drawdown_max_%          | 25.6   |
| t_stat                  | -2.83  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 14     |
| combinazioni            | 324    |
| drawdown_mediano_%      | 25.8   |
| drawdown_95%_dei_casi_% | 28.7   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                   |
|-------:|:--------------------------------------------------------------------------------------------|
|   2020 | {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 1.0, "uscita": 1170, "verso": 1}  |
|   2021 | {"decisione": 1080, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1230, "verso": 1}   |
|   2022 | {"decisione": 930, "inizio": 600, "soglia": 0.3, "stop": 0.5, "uscita": 1380, "verso": 1}   |
|   2023 | {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": -1} |
|   2024 | {"decisione": 1080, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1230, "verso": -1}  |
|   2025 | {"decisione": 930, "inizio": 90, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": -1}   |

## rottura_range

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1300   |
| vincenti_%              | 37.5   |
| R_medio                 | -0.077 |
| R_totale                | -100.4 |
| profit_factor           | 0.85   |
| rendimento_%            | -66.7  |
| drawdown_max_%          | 66.7   |
| t_stat                  | -2.29  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 72     |
| drawdown_mediano_%      | 70.6   |
| drawdown_95%_dei_casi_% | 75.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                                  |
|-------:|:-----------------------------------------------------------------------------------------------------------|
|   2020 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1}  |
|   2021 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": -1}  |
|   2022 | {"a": 1020, "da": 990, "fine_entrate": 1200, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1} |
|   2023 | {"a": 1020, "da": 990, "fine_entrate": 1200, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1}   |
|   2024 | {"a": 1020, "da": 990, "fine_entrate": 1200, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1}   |
|   2025 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1}    |

## ora_fissa

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 46.4   |
| R_medio                 | -0.029 |
| R_totale                | -38.9  |
| profit_factor           | 0.81   |
| rendimento_%            | -32.8  |
| drawdown_max_%          | 35.2   |
| t_stat                  | -2.94  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 34.9   |
| drawdown_95%_dei_casi_% | 38.2   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                 |
|-------:|:----------------------------------------------------------|
|   2020 | {"durata": 120, "entrata": 930, "stop": 1.0, "verso": 1}  |
|   2021 | {"durata": 240, "entrata": 930, "stop": 1.0, "verso": 1}  |
|   2022 | {"durata": 240, "entrata": 930, "stop": 1.0, "verso": -1} |
|   2023 | {"durata": 240, "entrata": 810, "stop": 1.0, "verso": 1}  |
|   2024 | {"durata": 240, "entrata": 570, "stop": 1.0, "verso": 1}  |
|   2025 | {"durata": 240, "entrata": 810, "stop": 1.0, "verso": 1}  |

## massimo_ieri

|                         | 0      |
|:------------------------|:-------|
| trade                   | 912    |
| vincenti_%              | 48.5   |
| R_medio                 | -0.018 |
| R_totale                | -16.0  |
| profit_factor           | 0.94   |
| rendimento_%            | -16.6  |
| drawdown_max_%          | 20.4   |
| t_stat                  | -0.76  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 26.8   |
| drawdown_95%_dei_casi_% | 34.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                        |
|-------:|:-----------------------------------------------------------------|
|   2020 | {"fine_entrate": 1170, "stop": 0.6, "uscita": 1380, "verso": -1} |
|   2021 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1230, "verso": 1}   |
|   2022 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": -1}  |
|   2023 | {"fine_entrate": 1170, "stop": 0.6, "uscita": 1230, "verso": -1} |
|   2024 | {"fine_entrate": 990, "stop": 0.6, "uscita": 1230, "verso": -1}  |
|   2025 | {"fine_entrate": 1170, "stop": 0.6, "uscita": 1230, "verso": -1} |

## trend_ema

|                         | 0     |
|:------------------------|:------|
| trade                   | 365   |
| vincenti_%              | 48.2  |
| R_medio                 | 0.044 |
| R_totale                | 16.2  |
| profit_factor           | 1.17  |
| rendimento_%            | 16.4  |
| drawdown_max_%          | 6.0   |
| t_stat                  | 1.14  |
| anni_in_utile           | 4/6   |
| griglia_pf_sopra_1_%    | 12    |
| combinazioni            | 24    |
| drawdown_mediano_%      | 9.9   |
| drawdown_95%_dei_casi_% | 15.1  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                |
|-------:|:-------------------------------------------------------------------------|
|   2020 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2025 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |

## bollinger

|                         | 0     |
|:------------------------|:------|
| trade                   | 486   |
| vincenti_%              | 43.8  |
| R_medio                 | 0.022 |
| R_totale                | 10.9  |
| profit_factor           | 1.05  |
| rendimento_%            | 8.2   |
| drawdown_max_%          | 26.8  |
| t_stat                  | 0.44  |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 19    |
| combinazioni            | 48    |
| drawdown_mediano_%      | 20.9  |
| drawdown_95%_dei_casi_% | 30.1  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                              |
|-------:|:---------------------------------------------------------------------------------------|
|   2020 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.5, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.5, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": 240, "k": 2.0, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60} |
|   2025 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60} |

## ichimoku

|                         | 0      |
|:------------------------|:-------|
| trade                   | 565    |
| vincenti_%              | 36.8   |
| R_medio                 | -0.056 |
| R_totale                | -31.6  |
| profit_factor           | 0.89   |
| rendimento_%            | -29.9  |
| drawdown_max_%          | 32.0   |
| t_stat                  | -1.12  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 39.1   |
| drawdown_95%_dei_casi_% | 47.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                          |
|-------:|:-----------------------------------------------------------------------------------|
|   2020 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2021 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60}  |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 430    |
| vincenti_%              | 41.6   |
| R_medio                 | -0.098 |
| R_totale                | -42.0  |
| profit_factor           | 0.75   |
| rendimento_%            | -35.3  |
| drawdown_max_%          | 37.5   |
| t_stat                  | -2.38  |
| anni_in_utile           | 0/6    |
| drawdown_mediano_%      | 38.4   |
| drawdown_95%_dei_casi_% | 43.2   |

|   anno | parametri                                                                                                     |
|-------:|:--------------------------------------------------------------------------------------------------------------|
|   2020 | momento_o_rientro {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 1.0, "uscita": 1170, "verso": 1}  |
|   2021 | momento_o_rientro {"decisione": 1080, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1230, "verso": 1}   |
|   2022 | momento_o_rientro {"decisione": 930, "inizio": 600, "soglia": 0.3, "stop": 0.5, "uscita": 1380, "verso": 1}   |
|   2023 | momento_o_rientro {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": -1} |
|   2024 | bollinger {"durata": 240, "k": 2.0, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60}              |
|   2025 | bollinger {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60}              |
