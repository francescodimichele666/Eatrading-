# Coppie opposte AUDUSD / USDCAD - 22/10/2026 08:55

Sviluppo fino al 01/04/2025. Rischio 1% a trade, take profit 2.5 volte lo stop. Costi cross: Costi(punto=1e-05, commissione_oncia=np.float64(0.0), spread_minimo_rel=0.0002494419115890295, slittamento_rel=4.2759322017715554e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| divergenza AUDUSDxUSDCAD                    |     464 |            0.92 |    -0.036 |    -0.72 | 1/6             |                      0 |                      37.6 |             48 |                 0 |
| conferma AUDUSD con USDCAD                  |     231 |            0.87 |    -0.029 |    -0.82 | 1/6             |                     25 |                      14.9 |             32 |                 0 |
| conferma USDCAD con AUDUSD                  |     153 |            1.08 |     0.023 |     0.37 | 3/6             |                     25 |                      12.6 |             32 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |     186 |            0.97 |    -0.008 |    -0.15 | 2/6             |                    nan |                      15.2 |            nan |               nan |

## divergenza AUDUSDxUSDCAD

|                         | 0      |
|:------------------------|:-------|
| trade                   | 464    |
| vincenti_%              | 42.7   |
| R_medio                 | -0.036 |
| R_totale                | -16.7  |
| profit_factor           | 0.92   |
| rendimento_%            | -17.6  |
| drawdown_max_%          | 29.0   |
| t_stat                  | -0.72  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 48     |
| drawdown_mediano_%      | 29.1   |
| drawdown_95%_dei_casi_% | 37.6   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                         |
|-------:|:------------------------------------------------------------------|
|   2020 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.0} |
|   2021 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2022 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2023 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2024 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |
|   2025 | {"durata": null, "finestra": 96, "stop": 2.0, "tf": 60, "z": 2.5} |

## conferma AUDUSD con USDCAD

|                         | 0      |
|:------------------------|:-------|
| trade                   | 231    |
| vincenti_%              | 44.2   |
| R_medio                 | -0.029 |
| R_totale                | -6.6   |
| profit_factor           | 0.87   |
| rendimento_%            | -6.7   |
| drawdown_max_%          | 10.0   |
| t_stat                  | -0.82  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 25     |
| combinazioni            | 32     |
| drawdown_mediano_%      | 11.0   |
| drawdown_95%_dei_casi_% | 14.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                      |
|-------:|:-------------------------------------------------------------------------------|
|   2020 | {"decisione": 1005, "inizio": 600, "soglia": 0.2, "stop": 1.0, "uscita": 1380} |
|   2021 | {"decisione": 930, "inizio": 90, "soglia": 0.4, "stop": 0.5, "uscita": 1230}   |
|   2022 | {"decisione": 930, "inizio": 600, "soglia": 0.4, "stop": 1.0, "uscita": 1380}  |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2024 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |
|   2025 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |

## conferma USDCAD con AUDUSD

|                         | 0     |
|:------------------------|:------|
| trade                   | 153   |
| vincenti_%              | 51.6  |
| R_medio                 | 0.023 |
| R_totale                | 3.6   |
| profit_factor           | 1.08  |
| rendimento_%            | 3.2   |
| drawdown_max_%          | 8.1   |
| t_stat                  | 0.37  |
| anni_in_utile           | 3/6   |
| griglia_pf_sopra_1_%    | 25    |
| combinazioni            | 32    |
| drawdown_mediano_%      | 8.3   |
| drawdown_95%_dei_casi_% | 12.6  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                                                                      |
|-------:|:-------------------------------------------------------------------------------|
|   2020 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2021 | {"decisione": 930, "inizio": 600, "soglia": 0.4, "stop": 1.0, "uscita": 1230}  |
|   2022 | {"decisione": 930, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380}  |
|   2023 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1380} |
|   2024 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |
|   2025 | {"decisione": 1005, "inizio": 600, "soglia": 0.4, "stop": 0.5, "uscita": 1230} |
