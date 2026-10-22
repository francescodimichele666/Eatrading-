# Ricerca su USDCHF (tutte) - 22/10/2026 08:44

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=0.00015839943463586407, slittamento_rel=2.4369143790132934e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| momento_o_rientro                           |     254 |            0.88 |    -0.02  |    -0.73 | 3/6             |                      6 |                      13.1 |            324 |                 0 |
| rottura_range                               |    1227 |            0.89 |    -0.069 |    -1.48 | 2/6             |                      0 |                      77.8 |             72 |                 0 |
| ora_fissa                                   |    1360 |            0.73 |    -0.039 |    -4.21 | 0/6             |                      0 |                      45   |             60 |                 0 |
| massimo_ieri                                |     926 |            0.86 |    -0.056 |    -1.77 | 1/6             |                      0 |                      56   |             24 |                 0 |
| trend_ema                                   |     443 |            0.69 |    -0.138 |    -3.07 | 1/6             |                      0 |                      52.9 |             24 |                 0 |
| bollinger                                   |     451 |            0.78 |    -0.111 |    -2.15 | 0/6             |                      0 |                      51   |             48 |                 0 |
| ichimoku                                    |     654 |            0.69 |    -0.14  |    -3.81 | 1/6             |                      0 |                      66   |             24 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     254 |            0.88 |    -0.02  |    -0.73 | 3/6             |                    nan |                      13.1 |            nan |               nan |

## momento_o_rientro

|                         | 0     |
|:------------------------|:------|
| trade                   | 254   |
| vincenti_%              | 47.2  |
| R_medio                 | -0.02 |
| R_totale                | -5.2  |
| profit_factor           | 0.88  |
| rendimento_%            | -5.3  |
| drawdown_max_%          | 9.1   |
| t_stat                  | -0.73 |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 6     |
| combinazioni            | 324   |
| drawdown_mediano_%      | 9.6   |
| drawdown_95%_dei_casi_% | 13.1  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                  |
|-------:|:-------------------------------------------------------------------------------------------|
|   2020 | {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1} |
|   2021 | {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1} |
|   2022 | {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1} |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1230, "verso": 1} |
|   2024 | {"decisione": 930, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1}  |
|   2025 | {"decisione": 930, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1}  |

## rottura_range

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1227   |
| vincenti_%              | 32.7   |
| R_medio                 | -0.069 |
| R_totale                | -84.3  |
| profit_factor           | 0.89   |
| rendimento_%            | -63.2  |
| drawdown_max_%          | 69.6   |
| t_stat                  | -1.48  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 72     |
| drawdown_mediano_%      | 70.3   |
| drawdown_95%_dei_casi_% | 77.8   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                                 |
|-------:|:----------------------------------------------------------------------------------------------------------|
|   2020 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1} |
|   2021 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}    |
|   2022 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1380, "verso": 1}    |
|   2023 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1}   |
|   2024 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1}   |
|   2025 | {"a": 600, "da": 180, "fine_entrate": 780, "stop": "opposto", "target": 0, "uscita": 1380, "verso": -1}   |

## ora_fissa

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 45.2   |
| R_medio                 | -0.039 |
| R_totale                | -53.1  |
| profit_factor           | 0.73   |
| rendimento_%            | -41.6  |
| drawdown_max_%          | 42.0   |
| t_stat                  | -4.21  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 42.8   |
| drawdown_95%_dei_casi_% | 45.0   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                  |
|-------:|:-----------------------------------------------------------|
|   2020 | {"durata": 240, "entrata": 1050, "stop": 1.0, "verso": -1} |
|   2021 | {"durata": 240, "entrata": 570, "stop": 1.0, "verso": -1}  |
|   2022 | {"durata": 240, "entrata": 810, "stop": 1.0, "verso": -1}  |
|   2023 | {"durata": 240, "entrata": 1050, "stop": 1.0, "verso": 1}  |
|   2024 | {"durata": 240, "entrata": 810, "stop": 1.0, "verso": -1}  |
|   2025 | {"durata": 240, "entrata": 930, "stop": 1.0, "verso": 1}   |

## massimo_ieri

|                         | 0      |
|:------------------------|:-------|
| trade                   | 926    |
| vincenti_%              | 42.4   |
| R_medio                 | -0.056 |
| R_totale                | -52.0  |
| profit_factor           | 0.86   |
| rendimento_%            | -43.1  |
| drawdown_max_%          | 49.0   |
| t_stat                  | -1.77  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 48.9   |
| drawdown_95%_dei_casi_% | 56.0   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                       |
|-------:|:----------------------------------------------------------------|
|   2020 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1230, "verso": -1} |
|   2021 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1230, "verso": 1}  |
|   2022 | {"fine_entrate": 990, "stop": 0.3, "uscita": 1230, "verso": 1}  |
|   2023 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1230, "verso": 1}  |
|   2024 | {"fine_entrate": 990, "stop": 0.6, "uscita": 1380, "verso": 1}  |
|   2025 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": 1}  |

## trend_ema

|                         | 0      |
|:------------------------|:-------|
| trade                   | 443    |
| vincenti_%              | 37.5   |
| R_medio                 | -0.138 |
| R_totale                | -61.3  |
| profit_factor           | 0.69   |
| rendimento_%            | -46.9  |
| drawdown_max_%          | 49.0   |
| t_stat                  | -3.07  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 24     |
| drawdown_mediano_%      | 49.0   |
| drawdown_95%_dei_casi_% | 52.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                 |
|-------:|:--------------------------------------------------------------------------|
|   2020 | {"durata": null, "medie": [9, 21], "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2021 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2022 | {"durata": 240, "medie": [20, 50], "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2023 | {"durata": null, "medie": [20, 50], "stop": 1.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "medie": [20, 50], "stop": 1.0, "target": 2.5, "tf": 60} |
|   2025 | {"durata": 240, "medie": [20, 50], "stop": 1.5, "target": 2.5, "tf": 60}  |

## bollinger

|                         | 0      |
|:------------------------|:-------|
| trade                   | 451    |
| vincenti_%              | 37.5   |
| R_medio                 | -0.111 |
| R_totale                | -50.2  |
| profit_factor           | 0.78   |
| rendimento_%            | -41.1  |
| drawdown_max_%          | 43.4   |
| t_stat                  | -2.15  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 48     |
| drawdown_mediano_%      | 45.2   |
| drawdown_95%_dei_casi_% | 51.0   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                              |
|-------:|:---------------------------------------------------------------------------------------|
|   2020 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2022 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": null, "k": 2.0, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2025 | {"durata": null, "k": 2.5, "oscillatore": "rsi", "stop": 2.0, "target": 2.5, "tf": 60} |

## ichimoku

|                         | 0     |
|:------------------------|:------|
| trade                   | 654   |
| vincenti_%              | 37.8  |
| R_medio                 | -0.14 |
| R_totale                | -91.8 |
| profit_factor           | 0.69  |
| rendimento_%            | -61.2 |
| drawdown_max_%          | 63.8  |
| t_stat                  | -3.81 |
| anni_in_utile           | 1/6   |
| griglia_pf_sopra_1_%    | 0     |
| combinazioni            | 24    |
| drawdown_mediano_%      | 62.8  |
| drawdown_95%_dei_casi_% | 66.0  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                          |
|-------:|:-----------------------------------------------------------------------------------|
|   2020 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.5, "target": 2.5, "tf": 60} |
|   2021 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.5, "target": 2.5, "tf": 60}     |
|   2022 | {"durata": null, "segnale_tipo": "incrocio", "stop": 2.0, "target": 2.5, "tf": 60} |
|   2023 | {"durata": 240, "segnale_tipo": "kumo", "stop": 2.0, "target": 2.5, "tf": 60}      |
|   2024 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.5, "target": 2.5, "tf": 60} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0     |
|:------------------------|:------|
| trade                   | 254   |
| vincenti_%              | 47.2  |
| R_medio                 | -0.02 |
| R_totale                | -5.2  |
| profit_factor           | 0.88  |
| rendimento_%            | -5.3  |
| drawdown_max_%          | 9.1   |
| t_stat                  | -0.73 |
| anni_in_utile           | 3/6   |
| drawdown_mediano_%      | 9.6   |
| drawdown_95%_dei_casi_% | 13.1  |

|   anno | parametri                                                                                                    |
|-------:|:-------------------------------------------------------------------------------------------------------------|
|   2020 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1} |
|   2021 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1} |
|   2022 | momento_o_rientro {"decisione": 1080, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1170, "verso": 1} |
|   2023 | momento_o_rientro {"decisione": 1005, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1230, "verso": 1} |
|   2024 | momento_o_rientro {"decisione": 930, "inizio": 600, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1}  |
|   2025 | momento_o_rientro {"decisione": 930, "inizio": 600, "soglia": 0.6, "stop": 1.0, "uscita": 1380, "verso": 1}  |
