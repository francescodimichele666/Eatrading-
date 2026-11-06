# Ricerca su EURUSD (pubblicate_forex) - 22/10/2026 10:06

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=9.786651008025054e-05, slittamento_rel=1.7793910923681917e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| ore_locali_breedon                          |    1360 |            0.98 |    -0.003 |    -0.27 | 4/6             |                     17 |                      25.4 |              6 |                 0 |
| fixing_krohn                                |    1360 |            0.87 |    -0.018 |    -1.85 | 0/6             |                      0 |                      31.1 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1360 |            0.98 |    -0.003 |    -0.27 | 4/6             |                    nan |                      25.4 |            nan |               nan |

## ore_locali_breedon

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 49.6   |
| R_medio                 | -0.003 |
| R_totale                | -4.5   |
| profit_factor           | 0.98   |
| rendimento_%            | -5.7   |
| drawdown_max_%          | 15.2   |
| t_stat                  | -0.27  |
| anni_in_utile           | 4/6    |
| griglia_pf_sopra_1_%    | 17     |
| combinazioni            | 6      |
| drawdown_mediano_%      | 18.5   |
| drawdown_95%_dei_casi_% | 25.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                           |
|-------:|:------------------------------------|
|   2020 | {"finestra": "europa", "stop": 0.5} |
|   2021 | {"finestra": "europa", "stop": 1.0} |
|   2022 | {"finestra": "europa", "stop": 1.0} |
|   2023 | {"finestra": "europa", "stop": 1.0} |
|   2024 | {"finestra": "europa", "stop": 1.0} |
|   2025 | {"finestra": "europa", "stop": 1.0} |

## fixing_krohn

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.7   |
| R_medio                 | -0.018 |
| R_totale                | -24.8  |
| profit_factor           | 0.87   |
| rendimento_%            | -22.7  |
| drawdown_max_%          | 23.6   |
| t_stat                  | -1.85  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 4      |
| drawdown_mediano_%      | 26.4   |
| drawdown_95%_dei_casi_% | 31.1   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2020 | {"fase": "dopo", "stop": 1.0}  |
|   2021 | {"fase": "prima", "stop": 1.0} |
|   2022 | {"fase": "prima", "stop": 1.0} |
|   2023 | {"fase": "prima", "stop": 1.0} |
|   2024 | {"fase": "prima", "stop": 1.0} |
|   2025 | {"fase": "prima", "stop": 1.0} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 49.6   |
| R_medio                 | -0.003 |
| R_totale                | -4.5   |
| profit_factor           | 0.98   |
| rendimento_%            | -5.7   |
| drawdown_max_%          | 15.2   |
| t_stat                  | -0.27  |
| anni_in_utile           | 4/6    |
| drawdown_mediano_%      | 18.5   |
| drawdown_95%_dei_casi_% | 25.4   |

|   anno | parametri                                              |
|-------:|:-------------------------------------------------------|
|   2020 | ore_locali_breedon {"finestra": "europa", "stop": 0.5} |
|   2021 | ore_locali_breedon {"finestra": "europa", "stop": 1.0} |
|   2022 | ore_locali_breedon {"finestra": "europa", "stop": 1.0} |
|   2023 | ore_locali_breedon {"finestra": "europa", "stop": 1.0} |
|   2024 | ore_locali_breedon {"finestra": "europa", "stop": 1.0} |
|   2025 | ore_locali_breedon {"finestra": "europa", "stop": 1.0} |
