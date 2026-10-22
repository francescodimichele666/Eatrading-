# Ricerca su USDCHF (pubblicate_forex) - 22/10/2026 10:06

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=1e-05, commissione_oncia=0.0, spread_minimo_rel=0.00015839943463586407, slittamento_rel=2.4369143790132934e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| ore_locali_breedon                          |    1360 |            0.82 |    -0.038 |    -2.73 | 1/6             |                      0 |                      48.6 |              6 |                 0 |
| fixing_krohn                                |    1360 |            0.68 |    -0.041 |    -5.05 | 0/6             |                      0 |                      45.9 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1360 |            0.82 |    -0.038 |    -2.73 | 1/6             |                    nan |                      48.6 |            nan |               nan |

## ore_locali_breedon

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 45.5   |
| R_medio                 | -0.038 |
| R_totale                | -52.1  |
| profit_factor           | 0.82   |
| rendimento_%            | -41.7  |
| drawdown_max_%          | 43.8   |
| t_stat                  | -2.73  |
| anni_in_utile           | 1/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 6      |
| drawdown_mediano_%      | 44.3   |
| drawdown_95%_dei_casi_% | 48.6   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                            |
|-------:|:-------------------------------------|
|   2020 | {"finestra": "europa", "stop": 0.5}  |
|   2021 | {"finestra": "europa", "stop": 0.5}  |
|   2022 | {"finestra": "america", "stop": 1.0} |
|   2023 | {"finestra": "europa", "stop": 1.0}  |
|   2024 | {"finestra": "europa", "stop": 1.0}  |
|   2025 | {"finestra": "europa", "stop": 1.0}  |

## fixing_krohn

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 43.1   |
| R_medio                 | -0.041 |
| R_totale                | -56.3  |
| profit_factor           | 0.68   |
| rendimento_%            | -43.4  |
| drawdown_max_%          | 43.9   |
| t_stat                  | -5.05  |
| anni_in_utile           | 0/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 4      |
| drawdown_mediano_%      | 44.2   |
| drawdown_95%_dei_casi_% | 45.9   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2020 | {"fase": "dopo", "stop": 1.0}  |
|   2021 | {"fase": "dopo", "stop": 1.0}  |
|   2022 | {"fase": "dopo", "stop": 1.0}  |
|   2023 | {"fase": "prima", "stop": 1.0} |
|   2024 | {"fase": "prima", "stop": 1.0} |
|   2025 | {"fase": "prima", "stop": 1.0} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1360   |
| vincenti_%              | 45.5   |
| R_medio                 | -0.038 |
| R_totale                | -52.1  |
| profit_factor           | 0.82   |
| rendimento_%            | -41.7  |
| drawdown_max_%          | 43.8   |
| t_stat                  | -2.73  |
| anni_in_utile           | 1/6    |
| drawdown_mediano_%      | 44.3   |
| drawdown_95%_dei_casi_% | 48.6   |

|   anno | parametri                                               |
|-------:|:--------------------------------------------------------|
|   2020 | ore_locali_breedon {"finestra": "europa", "stop": 0.5}  |
|   2021 | ore_locali_breedon {"finestra": "europa", "stop": 0.5}  |
|   2022 | ore_locali_breedon {"finestra": "america", "stop": 1.0} |
|   2023 | ore_locali_breedon {"finestra": "europa", "stop": 1.0}  |
|   2024 | ore_locali_breedon {"finestra": "europa", "stop": 1.0}  |
|   2025 | ore_locali_breedon {"finestra": "europa", "stop": 1.0}  |
