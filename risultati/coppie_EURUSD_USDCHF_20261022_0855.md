# Coppie opposte EURUSD / USDCHF - 22/10/2026 08:55

Sviluppo fino al 01/04/2025. Rischio 1% a trade, take profit 2.5 volte lo stop. Costi cross: Costi(punto=1e-05, commissione_oncia=np.float64(0.0), spread_minimo_rel=0.0002562659447161146, slittamento_rel=4.2163054713814855e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| divergenza EURUSDxUSDCHF                    |     381 |            0.65 |    -0.183 |    -3.51 | 1/6             |                      0 |                      56.4 |             48 |                 0 |
| conferma EURUSD con USDCHF                  |     338 |            0.85 |    -0.033 |    -1.1  | 3/6             |                     22 |                      20.2 |             32 |                 0 |
| conferma USDCHF con EURUSD                  |     307 |            0.87 |    -0.039 |    -0.93 | 2/6             |                      0 |                      23.4 |             32 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     338 |            0.85 |    -0.033 |    -1.1  | 3/6             |                    nan |                      20.2 |            nan |               nan |

## divergenza EURUSDxUSDCHF

|                         | 0      |
|:------------------------|:-------|
| trade                   | 381    |
| vincenti_%              | 32.8   |
| R_medio                 | -0.183 |
| R_totale                | -69.8  |
| profit_factor           | 0.65   |
| rendimento_%            | -51.2  |
| drawdown_max_%          | 55.1   |
| t_stat                  | -3.51  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 48     |
| drawdown_mediano_%      | 52.9   |
| drawdown_95%_dei_casi_% | 56.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                         |
|-------:|:------------------------------------------------------------------|
|   2020 | {"durata": null, "finestra": 96, "stop": 1.5, "tf": 60, "z": 2.5} |
|   2021 | {"durata": null, "finestra": 96, "stop": 1.5, "tf": 60, "z": 2.5} |
|   2022 | {"durata": null, "finestra": 96, "stop": 1.5, "tf": 60, "z": 2.5} |
|   2023 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2024 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2025 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |

## conferma EURUSD con USDCHF

|                         | 0      |
|:------------------------|:-------|
| trade                   | 338    |
| vincenti_%              | 46.7   |
| R_medio                 | -0.033 |
| R_totale                | -11.1  |
| profit_factor           | 0.85   |
| rendimento_%            | -11.0  |
| drawdown_max_%          | 14.9   |
| t_stat                  | -1.1   |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 22     |
| combinazioni            | 32     |
| drawdown_mediano_%      | 15.6   |
| drawdown_95%_dei_casi_% | 20.2   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                      |
|-------:|:-------------------------------------------------------------------------------|
|   2020 | {"decisione": 1005, "inizio": 90, "soglia": 0.2, "stop": 1.0, "uscita": 1380}  |
|   2021 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 1.0, "uscita": 1230} |
|   2022 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |
|   2024 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2025 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |

## conferma USDCHF con EURUSD

|                         | 0      |
|:------------------------|:-------|
| trade                   | 307    |
| vincenti_%              | 45.6   |
| R_medio                 | -0.039 |
| R_totale                | -11.9  |
| profit_factor           | 0.87   |
| rendimento_%            | -11.9  |
| drawdown_max_%          | 15.8   |
| t_stat                  | -0.93  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 32     |
| drawdown_mediano_%      | 17.9   |
| drawdown_95%_dei_casi_% | 23.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                      |
|-------:|:-------------------------------------------------------------------------------|
|   2020 | {"decisione": 1005, "inizio": 90, "soglia": 0.4, "stop": 0.5, "uscita": 1380}  |
|   2021 | {"decisione": 930, "inizio": 600, "soglia": 0.4, "stop": 1.0, "uscita": 1230}  |
|   2022 | {"decisione": 1005, "inizio": 600, "soglia": 0.2, "stop": 0.5, "uscita": 1380} |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2024 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2025 | {"decisione": 930, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380}  |
