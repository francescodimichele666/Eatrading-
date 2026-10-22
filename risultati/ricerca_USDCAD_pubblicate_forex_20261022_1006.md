# Ricerca su USDCAD (pubblicate_forex) - 22/10/2026 10:06

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.272666319536083e-05, slittamento_rel=1.4265640491593972e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| ore_locali_breedon                          |       0 |          nan    |   nan     |     0    | -               |                      0 |                     nan   |              6 |                 0 |
| fixing_krohn                                |    1360 |            0.83 |    -0.027 |    -2.46 | 0/6             |                      0 |                      38.5 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1360 |            0.83 |    -0.027 |    -2.46 | 0/6             |                    nan |                      38.5 |            nan |               nan |

## ore_locali_breedon

|                      | 0     |
|:---------------------|:------|
| trade                | 0     |
| t_stat               | 0     |
| anni_in_utile        | -     |
| griglia_pf_sopra_1_% | 0     |
| combinazioni         | 6     |
| supera_sviluppo      | False |

Parametri scelti nel walk-forward:



## fixing_krohn

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.1   |
| R_medio                 | -0.027 |
| R_totale                | -37.0  |
| profit_factor           | 0.83   |
| rendimento_%            | -31.7  |
| drawdown_max_%          | 32.9   |
| t_stat                  | -2.46  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 4      |
| drawdown_mediano_%      | 34.5   |
| drawdown_95%_dei_casi_% | 38.5   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2020 | {"fase": "dopo", "stop": 1.0}  |
|   2021 | {"fase": "dopo", "stop": 1.0}  |
|   2022 | {"fase": "dopo", "stop": 0.5}  |
|   2023 | {"fase": "prima", "stop": 1.0} |
|   2024 | {"fase": "dopo", "stop": 0.5}  |
|   2025 | {"fase": "prima", "stop": 1.0} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.1   |
| R_medio                 | -0.027 |
| R_totale                | -37.0  |
| profit_factor           | 0.83   |
| rendimento_%            | -31.7  |
| drawdown_max_%          | 32.9   |
| t_stat                  | -2.46  |
| anni_in_utile           | 0/6    |
| drawdown_mediano_%      | 34.5   |
| drawdown_95%_dei_casi_% | 38.5   |

|   anno | parametri                                   |
|-------:|:--------------------------------------------|
|   2020 | fixing_krohn {"fase": "dopo", "stop": 1.0}  |
|   2021 | fixing_krohn {"fase": "dopo", "stop": 1.0}  |
|   2022 | fixing_krohn {"fase": "dopo", "stop": 0.5}  |
|   2023 | fixing_krohn {"fase": "prima", "stop": 1.0} |
|   2024 | fixing_krohn {"fase": "dopo", "stop": 0.5}  |
|   2025 | fixing_krohn {"fase": "prima", "stop": 1.0} |
