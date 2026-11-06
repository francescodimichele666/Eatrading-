# Ricerca su XAUUSD.r (tutte) - 22/10/2026 08:20

Dati 02/07/2017 - 21/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=0.01, commissione_oncia=0.07, spread_minimo_rel=2.1760154738878142e-05, slittamento_rel=2.4177949709864606e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| momento_o_rientro                           |     874 |            1.04 |     0.013 |     0.45 | 4/6             |                     39 |                      30   |            324 |                 0 |
| rottura_range                               |    1222 |            1.03 |     0.014 |     0.34 | 3/6             |                     14 |                      54.9 |             72 |                 0 |
| ora_fissa                                   |    1353 |            0.99 |    -0.001 |    -0.19 | 3/6             |                      2 |                      12.9 |             60 |                 0 |
| massimo_ieri                                |     944 |            0.93 |    -0.034 |    -0.89 | 1/6             |                     21 |                      54.4 |             24 |                 0 |
| trend_ema                                   |     478 |            1.15 |     0.066 |     1.24 | 4/6             |                     50 |                      25.7 |             24 |                 0 |
| bollinger                                   |    1709 |            0.95 |    -0.03  |    -0.93 | 1/6             |                      0 |                      71.8 |             48 |                 0 |
| ichimoku                                    |     697 |            0.98 |    -0.014 |    -0.28 | 2/6             |                     25 |                      47.8 |             24 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     855 |            1.06 |     0.019 |     0.63 | 4/6             |                    nan |                      29.6 |            nan |               nan |

## momento_o_rientro

|                         | 0     |
|:------------------------|:------|
| trade                   | 874   |
| vincenti_%              | 48.9  |
| R_medio                 | 0.013 |
| R_totale                | 11.1  |
| profit_factor           | 1.04  |
| rendimento_%            | 8.5   |
| drawdown_max_%          | 24.5  |
| t_stat                  | 0.45  |
| anni_in_utile           | 4/6   |
| griglia_pf_sopra_1_%    | 39    |
| combinazioni            | 324   |
| drawdown_mediano_%      | 20.5  |
| drawdown_95%_dei_casi_% | 30.0  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                  |
|-------:|:-------------------------------------------------------------------------------------------|
|   2020 | {"decisione": 1080, "inizio": 90, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}  |
|   2021 | {"decisione": 930, "inizio": 90, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}   |
|   2022 | {"decisione": 930, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1} |
|   2023 | {"decisione": 930, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1} |
|   2024 | {"decisione": 1005, "inizio": 600, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": 1} |
|   2025 | {"decisione": 1005, "inizio": 900, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1} |

## rottura_range

|                         | 0     |
|:------------------------|:------|
| trade                   | 1222  |
| vincenti_%              | 39.2  |
| R_medio                 | 0.014 |
| R_totale                | 17.6  |
| profit_factor           | 1.03  |
| rendimento_%            | 4.5   |
| drawdown_max_%          | 41.9  |
| t_stat                  | 0.34  |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 14    |
| combinazioni            | 72    |
| drawdown_mediano_%      | 40.8  |
| drawdown_95%_dei_casi_% | 54.9  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                                                 |
|-------:|:----------------------------------------------------------------------------------------------------------|
|   2020 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}    |
|   2021 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}    |
|   2022 | {"a": 660, "da": 600, "fine_entrate": 840, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}    |
|   2023 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 0, "uscita": 1230, "verso": 1}   |
|   2024 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1} |
|   2025 | {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1} |

## ora_fissa

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1353   |
| vincenti_%              | 50.7   |
| R_medio                 | -0.001 |
| R_totale                | -1.5   |
| profit_factor           | 0.99   |
| rendimento_%            | -1.8   |
| drawdown_max_%          | 15.1   |
| t_stat                  | -0.19  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 2      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 8.8    |
| drawdown_95%_dei_casi_% | 12.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                 |
|-------:|:----------------------------------------------------------|
|   2020 | {"durata": 240, "entrata": 570, "stop": 1.0, "verso": 1}  |
|   2021 | {"durata": 240, "entrata": 570, "stop": 1.0, "verso": 1}  |
|   2022 | {"durata": 60, "entrata": 1050, "stop": 1.0, "verso": 1}  |
|   2023 | {"durata": 240, "entrata": 690, "stop": 1.0, "verso": -1} |
|   2024 | {"durata": 120, "entrata": 210, "stop": 1.0, "verso": 1}  |
|   2025 | {"durata": 120, "entrata": 690, "stop": 1.0, "verso": 1}  |

## massimo_ieri

|                         | 0      |
|:------------------------|:-------|
| trade                   | 944    |
| vincenti_%              | 39.9   |
| R_medio                 | -0.034 |
| R_totale                | -32.1  |
| profit_factor           | 0.93   |
| rendimento_%            | -32.0  |
| drawdown_max_%          | 39.0   |
| t_stat                  | -0.89  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 21     |
| combinazioni            | 24     |
| drawdown_mediano_%      | 44.4   |
| drawdown_95%_dei_casi_% | 54.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                        |
|-------:|:-----------------------------------------------------------------|
|   2020 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": -1}  |
|   2021 | {"fine_entrate": 1170, "stop": 0.3, "uscita": 1230, "verso": 1}  |
|   2022 | {"fine_entrate": 1170, "stop": 0.3, "uscita": 1380, "verso": 1}  |
|   2023 | {"fine_entrate": 990, "stop": 1.0, "uscita": 1380, "verso": 1}   |
|   2024 | {"fine_entrate": 1170, "stop": 0.3, "uscita": 1230, "verso": -1} |
|   2025 | {"fine_entrate": 1170, "stop": 0.3, "uscita": 1230, "verso": -1} |

## trend_ema

|                         | 0     |
|:------------------------|:------|
| trade                   | 478   |
| vincenti_%              | 44.8  |
| R_medio                 | 0.066 |
| R_totale                | 31.5  |
| profit_factor           | 1.15  |
| rendimento_%            | 32.7  |
| drawdown_max_%          | 19.4  |
| t_stat                  | 1.24  |
| anni_in_utile           | 4/6   |
| griglia_pf_sopra_1_%    | 50    |
| combinazioni            | 24    |
| drawdown_mediano_%      | 17.0  |
| drawdown_95%_dei_casi_% | 25.7  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                 |
|-------:|:--------------------------------------------------------------------------|
|   2020 | {"durata": null, "medie": [20, 50], "stop": 1.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": 240, "medie": [20, 50], "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2022 | {"durata": 240, "medie": [20, 50], "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2023 | {"durata": null, "medie": [9, 21], "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2024 | {"durata": null, "medie": [9, 21], "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": null, "medie": [9, 21], "stop": 2.0, "target": 2.5, "tf": 60}  |

## bollinger

|                         | 0     |
|:------------------------|:------|
| trade                   | 1709  |
| vincenti_%              | 36.0  |
| R_medio                 | -0.03 |
| R_totale                | -51.7 |
| profit_factor           | 0.95  |
| rendimento_%            | -48.8 |
| drawdown_max_%          | 51.7  |
| t_stat                  | -0.93 |
| anni_in_utile           | 1/6   |
| griglia_pf_sopra_1_%    | 0     |
| combinazioni            | 48    |
| drawdown_mediano_%      | 61.8  |
| drawdown_95%_dei_casi_% | 71.8  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                               |
|-------:|:----------------------------------------------------------------------------------------|
|   2020 | {"durata": null, "k": 2.0, "oscillatore": "stoc", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2021 | {"durata": 240, "k": 2.0, "oscillatore": "stoc", "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2022 | {"durata": null, "k": 2.0, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 15} |
|   2023 | {"durata": null, "k": 2.5, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 15} |
|   2024 | {"durata": 240, "k": 2.0, "oscillatore": "stoc", "stop": 2.0, "target": 2.5, "tf": 60}  |
|   2025 | {"durata": 240, "k": 2.5, "oscillatore": "stoc", "stop": 1.5, "target": 2.5, "tf": 60}  |

## ichimoku

|                         | 0      |
|:------------------------|:-------|
| trade                   | 697    |
| vincenti_%              | 37.2   |
| R_medio                 | -0.014 |
| R_totale                | -9.7   |
| profit_factor           | 0.98   |
| rendimento_%            | -14.7  |
| drawdown_max_%          | 43.4   |
| t_stat                  | -0.28  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 25     |
| combinazioni            | 24     |
| drawdown_mediano_%      | 36.3   |
| drawdown_95%_dei_casi_% | 47.8   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                          |
|-------:|:-----------------------------------------------------------------------------------|
|   2020 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.0, "target": 2.5, "tf": 60}     |
|   2021 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.0, "target": 2.5, "tf": 60}     |
|   2022 | {"durata": 240, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60}  |
|   2023 | {"durata": null, "segnale_tipo": "incrocio", "stop": 1.0, "target": 2.5, "tf": 60} |
|   2024 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.5, "target": 2.5, "tf": 60}     |
|   2025 | {"durata": null, "segnale_tipo": "kumo", "stop": 1.5, "target": 2.5, "tf": 60}     |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0     |
|:------------------------|:------|
| trade                   | 855   |
| vincenti_%              | 49.4  |
| R_medio                 | 0.019 |
| R_totale                | 16.0  |
| profit_factor           | 1.06  |
| rendimento_%            | 13.7  |
| drawdown_max_%          | 27.5  |
| t_stat                  | 0.63  |
| anni_in_utile           | 4/6   |
| drawdown_mediano_%      | 20.4  |
| drawdown_95%_dei_casi_% | 29.6  |

|   anno | parametri                                                                                                               |
|-------:|:------------------------------------------------------------------------------------------------------------------------|
|   2020 | momento_o_rientro {"decisione": 1080, "inizio": 90, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}             |
|   2021 | momento_o_rientro {"decisione": 930, "inizio": 90, "soglia": 0.6, "stop": 1.0, "uscita": 1230, "verso": 1}              |
|   2022 | momento_o_rientro {"decisione": 930, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1}            |
|   2023 | momento_o_rientro {"decisione": 930, "inizio": 900, "soglia": 0.0, "stop": 0.5, "uscita": 1380, "verso": -1}            |
|   2024 | rottura_range {"a": 980, "da": 920, "fine_entrate": 1160, "stop": "opposto", "target": 2.0, "uscita": 1380, "verso": 1} |
|   2025 | momento_o_rientro {"decisione": 1005, "inizio": 900, "soglia": 0.6, "stop": 0.5, "uscita": 1380, "verso": 1}            |
