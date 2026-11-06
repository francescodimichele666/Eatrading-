# Ricerca su AUDUSD (tutte) - 22/10/2026 08:44

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=0.0001567152483936687, slittamento_rel=2.8493681526121582e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| momento_o_rientro                           |     227 |            0.88 |    -0.03  |    -0.8  | 3/6             |                      6 |                      15.7 |            324 |                 0 |
| rottura_range                               |    1028 |            0.85 |    -0.092 |    -1.94 | 1/6             |                      0 |                      76.5 |             72 |                 0 |
| ora_fissa                                   |    1360 |            0.77 |    -0.026 |    -3.49 | 1/6             |                      0 |                      33.5 |             60 |                 0 |
| massimo_ieri                                |     869 |            0.81 |    -0.088 |    -2.49 | 0/6             |                      0 |                      64.6 |             24 |                 0 |
| trend_ema                                   |     506 |            0.9  |    -0.046 |    -0.94 | 2/6             |                      0 |                      41.4 |             24 |                 0 |
| bollinger                                   |     796 |            0.99 |    -0.006 |    -0.16 | 3/6             |                      0 |                      38.6 |             48 |                 0 |
| ichimoku                                    |     683 |            0.84 |    -0.082 |    -1.91 | 0/6             |                      0 |                      56.9 |             24 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     227 |            0.88 |    -0.03  |    -0.8  | 3/6             |                    nan |                      15.7 |            nan |               nan |

## momento_o_rientro

|                         | 0     |
|:------------------------|:------|
| trade                   | 227   |
| vincenti_%              | 48.5  |
| R_medio                 | -0.03 |
| R_totale                | -6.8  |
| profit_factor           | 0.88  |
| rendimento_%            | -6.9  |
| drawdown_max_%          | 13.2  |
| t_stat                  | -0.8  |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 6     |
| combinazioni            | 324   |
| drawdown_mediano_%      | 11.6  |
| drawdown_95%_dei_casi_% | 15.7  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                  |
|-------:|:-------------------------------------------------------------------------------------------|
|   2020 | {"decisione": 1080, "inizio": 600, "soglia": 0.3, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2021 | {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1} |
|   2022 | {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1} |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2024 | {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2025 | {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": -1} |

## rottura_range

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1028   |
| vincenti_%              | 32.8   |
| R_medio                 | -0.092 |
| R_totale                | -94.6  |
| profit_factor           | 0.85   |
| rendimento_%            | -65.4  |
| drawdown_max_%          | 68.1   |
| t_stat                  | -1.94  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 72     |
| drawdown_mediano_%      | 70.1   |
| drawdown_95%_dei_casi_% | 76.5   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                                |
|-------:|:---------------------------------------------------------------------------------------------------------|
|   2020 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "meta", "target": 0, "uscita": 1380, "verso": 1}      |
|   2021 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "meta", "target": 0, "uscita": 1380, "verso": 1}      |
|   2022 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}   |
|   2023 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}   |
|   2024 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1}  |
|   2025 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1} |

## ora_fissa

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.3   |
| R_medio                 | -0.026 |
| R_totale                | -35.0  |
| profit_factor           | 0.77   |
| rendimento_%            | -29.9  |
| drawdown_max_%          | 31.1   |
| t_stat                  | -3.49  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 31.3   |
| drawdown_95%_dei_casi_% | 33.5   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                 |
|-------:|:----------------------------------------------------------|
|   2020 | {"durata": 240, "entrata": 210, "stop": 1.0, "verso": 1}  |
|   2021 | {"durata": 240, "entrata": 210, "stop": 1.0, "verso": 1}  |
|   2022 | {"durata": 240, "entrata": 930, "stop": 1.0, "verso": 1}  |
|   2023 | {"durata": 240, "entrata": 90, "stop": 1.0, "verso": -1}  |
|   2024 | {"durata": 240, "entrata": 690, "stop": 1.0, "verso": -1} |
|   2025 | {"durata": 240, "entrata": 690, "stop": 1.0, "verso": -1} |

## massimo_ieri

|                         | 0      |
|:------------------------|:-------|
| trade                   | 869    |
| vincenti_%              | 40.0   |
| R_medio                 | -0.088 |
| R_totale                | -76.7  |
| profit_factor           | 0.81   |
| rendimento_%            | -55.7  |
| drawdown_max_%          | 56.3   |
| t_stat                  | -2.49  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 59.2   |
| drawdown_95%_dei_casi_% | 64.6   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                       |
|-------:|:----------------------------------------------------------------|
|   2020 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1230, "verso": -1} |
|   2021 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1230, "verso": -1} |
|   2022 | {"fine_entrate": 990, "stop": 0.6, "uscita": 1380, "verso": 1}  |
|   2023 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1380, "verso": -1} |
|   2024 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": -1} |
|   2025 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": -1} |

## trend_ema

|                         | 0      |
|:------------------------|:-------|
| trade                   | 506    |
| vincenti_%              | 40.5   |
| R_medio                 | -0.046 |
| R_totale                | -23.2  |
| profit_factor           | 0.9    |
| rendimento_%            | -23.1  |
| drawdown_max_%          | 33.3   |
| t_stat                  | -0.94  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 32.8   |
| drawdown_95%_dei_casi_% | 41.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                 |
|-------:|:--------------------------------------------------------------------------|
|   2020 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "medie": [20, 50], "stop": 1.5, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "medie": [9, 21], "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2024 | {"durata": null, "medie": [9, 21], "stop": 1.5, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": null, "medie": [9, 21], "stop": 1.5, "target": 2.5, "tf": 60}  |

## bollinger

|                         | 0      |
|:------------------------|:-------|
| trade                   | 796    |
| vincenti_%              | 43.7   |
| R_medio                 | -0.006 |
| R_totale                | -4.6   |
| profit_factor           | 0.99   |
| rendimento_%            | -8.0   |
| drawdown_max_%          | 24.4   |
| t_stat                  | -0.16  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 48     |
| drawdown_mediano_%      | 28.1   |
| drawdown_95%_dei_casi_% | 38.6   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                               |
|-------:|:----------------------------------------------------------------------------------------|
|   2020 | {"durata": null, "k": 2.0, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "k": 2.0, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "k": 2.5, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "k": 2.0, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": 240, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60}   |

## ichimoku

|                         | 0      |
|:------------------------|:-------|
| trade                   | 683    |
| vincenti_%              | 39.4   |
| R_medio                 | -0.082 |
| R_totale                | -55.8  |
| profit_factor           | 0.84   |
| rendimento_%            | -45.2  |
| drawdown_max_%          | 47.8   |
| t_stat                  | -1.91  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 50.3   |
| drawdown_95%_dei_casi_% | 56.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                          |
|-------:|:-----------------------------------------------------------------------------------|
|   2020 | {"durata": null, "segnale_tipo": "kumo", "stop": 2.0, "target": 2.5, "tf": 60}     |
|   2021 | {"durata": null, "segnale_tipo": "kumo", "stop": 2.0, "target": 2.5, "tf": 60}     |
|   2022 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.5, "target": 2.5, "tf": 60}     |
|   2023 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.5, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.5, "target": 2.5, "tf": 60}     |
|   2025 | {"durata": 240, "segnale_tipo": "kumo", "stop": 1.0, "target": 2.5, "tf": 60}      |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0     |
|:------------------------|:------|
| trade                   | 227   |
| vincenti_%              | 48.5  |
| R_medio                 | -0.03 |
| R_totale                | -6.8  |
| profit_factor           | 0.88  |
| rendimento_%            | -6.9  |
| drawdown_max_%          | 13.2  |
| t_stat                  | -0.8  |
| anni_in_utile           | 3/6   |
| drawdown_mediano_%      | 11.6  |
| drawdown_95%_dei_casi_% | 15.7  |

|   anno | parametri                                                                                                    |
|-------:|:-------------------------------------------------------------------------------------------------------------|
|   2020 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.3, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2021 | momento_o_rientro {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1} |
|   2022 | momento_o_rientro {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1} |
|   2023 | momento_o_rientro {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2024 | momento_o_rientro {"decisione": 1080, "inizio": 900, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2025 | momento_o_rientro {"decisione": 1005, "inizio": 90, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": -1} |
