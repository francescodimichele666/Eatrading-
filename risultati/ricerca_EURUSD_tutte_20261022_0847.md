# Ricerca su EURUSD (tutte) - 22/10/2026 08:44

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.786651008025054e-05, slittamento_rel=1.7793910923681917e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| momento_o_rientro                           |     365 |            0.73 |    -0.053 |    -2.16 | 2/6             |                     14 |                      23.2 |            324 |                 0 |
| rottura_range                               |    1180 |            0.88 |    -0.067 |    -1.72 | 3/6             |                      0 |                      72.8 |             72 |                 0 |
| ora_fissa                                   |    1360 |            0.78 |    -0.021 |    -3.3  | 1/6             |                      0 |                      28.8 |             60 |                 0 |
| massimo_ieri                                |     899 |            0.9  |    -0.034 |    -1.22 | 2/6             |                      0 |                      45   |             24 |                 0 |
| trend_ema                                   |     331 |            0.99 |    -0.005 |    -0.09 | 4/6             |                      0 |                      25.1 |             24 |                 0 |
| bollinger                                   |     717 |            0.99 |    -0.004 |    -0.12 | 2/6             |                      0 |                      36.3 |             48 |                 0 |
| ichimoku                                    |     591 |            0.95 |    -0.025 |    -0.52 | 3/6             |                     12 |                      42.2 |             24 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     365 |            0.73 |    -0.053 |    -2.16 | 2/6             |                    nan |                      23.2 |            nan |               nan |

## momento_o_rientro

|                         | 0      |
|:------------------------|:-------|
| trade                   | 365    |
| vincenti_%              | 44.7   |
| R_medio                 | -0.053 |
| R_totale                | -19.2  |
| profit_factor           | 0.73   |
| rendimento_%            | -17.8  |
| drawdown_max_%          | 19.2   |
| t_stat                  | -2.16  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 14     |
| combinazioni            | 324    |
| drawdown_mediano_%      | 19.9   |
| drawdown_95%_dei_casi_% | 23.2   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                   |
|-------:|:--------------------------------------------------------------------------------------------|
|   2020 | {"decisione": 1080, "inizio": 900, "soglia": 0.3, "stop": 1.0, "uscita": 1380, "verso": 1}  |
|   2021 | {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}  |
|   2022 | {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1170, "verso": 1}  |
|   2023 | {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1}   |
|   2024 | {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1}   |
|   2025 | {"decisione": 1005, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1} |

## rottura_range

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1180   |
| vincenti_%              | 36.4   |
| R_medio                 | -0.067 |
| R_totale                | -79.1  |
| profit_factor           | 0.88   |
| rendimento_%            | -59.2  |
| drawdown_max_%          | 72.5   |
| t_stat                  | -1.72  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 72     |
| drawdown_mediano_%      | 65.4   |
| drawdown_95%_dei_casi_% | 72.8   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                               |
|-------:|:--------------------------------------------------------------------------------------------------------|
|   2020 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1} |
|   2021 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1} |
|   2022 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "meta", "target": 0, "uscita": 1380, "verso": 1}    |
|   2023 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}  |
|   2024 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1}  |
|   2025 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}  |

## ora_fissa

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 46.7   |
| R_medio                 | -0.021 |
| R_totale                | -28.3  |
| profit_factor           | 0.78   |
| rendimento_%            | -24.9  |
| drawdown_max_%          | 26.1   |
| t_stat                  | -3.3   |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 26.2   |
| drawdown_95%_dei_casi_% | 28.8   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                  |
|-------:|:-----------------------------------------------------------|
|   2020 | {"durata": 240, "entrata": 90, "stop": 1.0, "verso": 1}    |
|   2021 | {"durata": 240, "entrata": 90, "stop": 1.0, "verso": 1}    |
|   2022 | {"durata": 120, "entrata": 1050, "stop": 1.0, "verso": -1} |
|   2023 | {"durata": 240, "entrata": 690, "stop": 1.0, "verso": -1}  |
|   2024 | {"durata": 240, "entrata": 690, "stop": 1.0, "verso": -1}  |
|   2025 | {"durata": 240, "entrata": 810, "stop": 1.0, "verso": -1}  |

## massimo_ieri

|                         | 0      |
|:------------------------|:-------|
| trade                   | 899    |
| vincenti_%              | 45.5   |
| R_medio                 | -0.034 |
| R_totale                | -30.6  |
| profit_factor           | 0.9    |
| rendimento_%            | -28.6  |
| drawdown_max_%          | 38.2   |
| t_stat                  | -1.22  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 36.7   |
| drawdown_95%_dei_casi_% | 45.0   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                       |
|-------:|:----------------------------------------------------------------|
|   2020 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": -1} |
|   2021 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1230, "verso": -1} |
|   2022 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1230, "verso": -1} |
|   2023 | {"fine_entrate": 990, "stop": 0.6, "uscita": 1230, "verso": -1} |
|   2024 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1380, "verso": 1}  |
|   2025 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1380, "verso": 1}  |

## trend_ema

|                         | 0      |
|:------------------------|:-------|
| trade                   | 331    |
| vincenti_%              | 45.6   |
| R_medio                 | -0.005 |
| R_totale                | -1.6   |
| profit_factor           | 0.99   |
| rendimento_%            | -3.1   |
| drawdown_max_%          | 21.0   |
| t_stat                  | -0.09  |
| anni_in_utile           | 4/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 18.0   |
| drawdown_95%_dei_casi_% | 25.1   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                 |
|-------:|:--------------------------------------------------------------------------|
|   2020 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2025 | {"durata": 240, "medie": [20, 50], "stop": 1.5, "target": 2.5, "tf": 60}  |

## bollinger

|                         | 0      |
|:------------------------|:-------|
| trade                   | 717    |
| vincenti_%              | 45.2   |
| R_medio                 | -0.004 |
| R_totale                | -3.2   |
| profit_factor           | 0.99   |
| rendimento_%            | -6.3   |
| drawdown_max_%          | 21.3   |
| t_stat                  | -0.12  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 48     |
| drawdown_mediano_%      | 26.3   |
| drawdown_95%_dei_casi_% | 36.3   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                               |
|-------:|:----------------------------------------------------------------------------------------|
|   2020 | {"durata": null, "k": 2.5, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "k": 2.5, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "k": 2.5, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": 240, "k": 2.5, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2024 | {"durata": 240, "k": 2.5, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": 240, "k": 2.5, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60}  |

## ichimoku

|                         | 0      |
|:------------------------|:-------|
| trade                   | 591    |
| vincenti_%              | 40.6   |
| R_medio                 | -0.025 |
| R_totale                | -14.7  |
| profit_factor           | 0.95   |
| rendimento_%            | -17.0  |
| drawdown_max_%          | 42.0   |
| t_stat                  | -0.52  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 12     |
| combinazioni            | 24     |
| drawdown_mediano_%      | 32.2   |
| drawdown_95%_dei_casi_% | 42.2   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                          |
|-------:|:-----------------------------------------------------------------------------------|
|   2020 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2021 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2022 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.0, "target": 2.5, "tf": 60}     |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 365    |
| vincenti_%              | 44.7   |
| R_medio                 | -0.053 |
| R_totale                | -19.2  |
| profit_factor           | 0.73   |
| rendimento_%            | -17.8  |
| drawdown_max_%          | 19.2   |
| t_stat                  | -2.16  |
| anni_in_utile           | 2/6    |
| drawdown_mediano_%      | 19.9   |
| drawdown_95%_dei_casi_% | 23.2   |

|   anno | parametri                                                                                                     |
|-------:|:--------------------------------------------------------------------------------------------------------------|
|   2020 | momento_o_rientro {"decisione": 1080, "inizio": 900, "soglia": 0.3, "stop": 1.0, "uscita": 1380, "verso": 1}  |
|   2021 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}  |
|   2022 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1170, "verso": 1}  |
|   2023 | momento_o_rientro {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1}   |
|   2024 | momento_o_rientro {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1}   |
|   2025 | momento_o_rientro {"decisione": 1005, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1} |
