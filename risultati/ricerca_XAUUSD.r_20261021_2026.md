# Ricerca su XAUUSD.r - 21/10/2026 20:25

Dati 02/07/2017 - 21/10/2026; sviluppo fino al 01/04/2025. Costi: Costi(punto=0.01, commissione_oncia=0.07, spread_minimo_rel=2.1760154738878142e-05, slittamento_rel=2.4177949709864606e-05)

## Sintesi

| famiglia          |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni | supera_sviluppo   |
|:------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|:------------------|
| momento_o_rientro |     874 |            1.04 |     0.013 |     0.45 | 4/6             |                     39 |                      23.3 |            324 | False             |
| rottura_range     |    1222 |            1.03 |     0.014 |     0.34 | 3/6             |                     14 |                      44.6 |             72 | False             |
| ora_fissa         |    1353 |            0.99 |    -0.001 |    -0.19 | 3/6             |                      2 |                       9.8 |             60 | False             |
| massimo_ieri      |     944 |            0.93 |    -0.034 |    -0.89 | 1/6             |                     21 |                      44.1 |             24 | False             |

## momento_o_rientro

|                         | 0     |
|:------------------------|:------|
| trade                   | 874   |
| vincenti_%              | 48.9  |
| R_medio                 | 0.013 |
| R_totale                | 11.1  |
| profit_factor           | 1.04  |
| rendimento_%            | 6.9   |
| drawdown_max_%          | 18.8  |
| t_stat                  | 0.45  |
| anni_in_utile           | 4/6   |
| griglia_pf_sopra_1_%    | 39    |
| combinazioni            | 324   |
| drawdown_mediano_%      | 15.7  |
| drawdown_95%_dei_casi_% | 23.3  |
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
| rendimento_%            | 5.9   |
| drawdown_max_%          | 32.6  |
| t_stat                  | 0.34  |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 14    |
| combinazioni            | 72    |
| drawdown_mediano_%      | 32.1  |
| drawdown_95%_dei_casi_% | 44.6  |
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
| rendimento_%            | -1.3   |
| drawdown_max_%          | 11.5   |
| t_stat                  | -0.19  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 2      |
| combinazioni            | 60     |
| drawdown_mediano_%      | 6.7    |
| drawdown_95%_dei_casi_% | 9.8    |
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
| rendimento_%            | -24.2  |
| drawdown_max_%          | 30.5   |
| t_stat                  | -0.89  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 21     |
| combinazioni            | 24     |
| drawdown_mediano_%      | 35.1   |
| drawdown_95%_dei_casi_% | 44.1   |
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
