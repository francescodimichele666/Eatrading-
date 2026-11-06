# Ricerca su AUDUSD (pubblicate_forex) - 22/10/2026 10:06

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=0.0001567152483936687, slittamento_rel=2.8493681526121582e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| ore_locali_breedon                          |    1360 |            0.84 |    -0.039 |    -2.38 | 0/6             |                      0 |                      51.3 |              6 |                 0 |
| fixing_krohn                                |    1360 |            0.81 |    -0.038 |    -2.87 | 0/6             |                      0 |                      48.4 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1360 |            0.82 |    -0.045 |    -2.72 | 0/6             |                    nan |                      54.9 |            nan |               nan |

## ore_locali_breedon

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.4   |
| R_medio                 | -0.039 |
| R_totale                | -53.3  |
| profit_factor           | 0.84   |
| rendimento_%            | -42.8  |
| drawdown_max_%          | 47.3   |
| t_stat                  | -2.38  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 6      |
| drawdown_mediano_%      | 46.4   |
| drawdown_95%_dei_casi_% | 51.3   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                            |
|-------:|:-------------------------------------|
|   2020 | {"finestra": "america", "stop": 1.0} |
|   2021 | {"finestra": "america", "stop": 0.5} |
|   2022 | {"finestra": "america", "stop": 0.5} |
|   2023 | {"finestra": "asia", "stop": 0.5}    |
|   2024 | {"finestra": "asia", "stop": 0.5}    |
|   2025 | {"finestra": "asia", "stop": 0.5}    |

## fixing_krohn

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 46.3   |
| R_medio                 | -0.038 |
| R_totale                | -52.3  |
| profit_factor           | 0.81   |
| rendimento_%            | -41.7  |
| drawdown_max_%          | 47.6   |
| t_stat                  | -2.87  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 4      |
| drawdown_mediano_%      | 44.2   |
| drawdown_95%_dei_casi_% | 48.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2020 | {"fase": "prima", "stop": 0.5} |
|   2021 | {"fase": "prima", "stop": 0.5} |
|   2022 | {"fase": "prima", "stop": 1.0} |
|   2023 | {"fase": "prima", "stop": 1.0} |
|   2024 | {"fase": "prima", "stop": 1.0} |
|   2025 | {"fase": "prima", "stop": 0.5} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 47.0   |
| R_medio                 | -0.045 |
| R_totale                | -61.4  |
| profit_factor           | 0.82   |
| rendimento_%            | -47.3  |
| drawdown_max_%          | 50.0   |
| t_stat                  | -2.72  |
| anni_in_utile           | 0/6    |
| drawdown_mediano_%      | 50.2   |
| drawdown_95%_dei_casi_% | 54.9   |

|   anno | parametri                                               |
|-------:|:--------------------------------------------------------|
|   2020 | ore_locali_breedon {"finestra": "america", "stop": 1.0} |
|   2021 | ore_locali_breedon {"finestra": "america", "stop": 0.5} |
|   2022 | ore_locali_breedon {"finestra": "america", "stop": 0.5} |
|   2023 | ore_locali_breedon {"finestra": "asia", "stop": 0.5}    |
|   2024 | ore_locali_breedon {"finestra": "asia", "stop": 0.5}    |
|   2025 | fixing_krohn {"fase": "prima", "stop": 0.5}             |
