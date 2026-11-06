# Ricerca su US100 (pubblicate_indici) - 22/10/2026 10:06

Dati 06/05/2018 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=0.01, commissione_oncia=0.0, spread_minimo_rel=2.0486520723043847e-05, slittamento_rel=1.0243260361521923e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| orb_zarattini                               |    1089 |            1.12 |     0.092 |     1.3  | 4/5             |                    100 |                      60.3 |              2 |                 0 |
| ultima_mezzora_gao                          |     571 |            0.83 |    -0.02  |    -1.66 | 2/5             |                      0 |                      16.6 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1089 |            1.12 |     0.092 |     1.3  | 4/5             |                    nan |                      60.3 |            nan |               nan |

## orb_zarattini

|                         | 0     |
|:------------------------|:------|
| trade                   | 1089  |
| vincenti_%              | 23.6  |
| R_medio                 | 0.092 |
| R_totale                | 99.7  |
| profit_factor           | 1.12  |
| rendimento_%            | 103.9 |
| drawdown_max_%          | 33.3  |
| t_stat                  | 1.3   |
| anni_in_utile           | 4/5   |
| griglia_pf_sopra_1_%    | 100   |
| combinazioni            | 2     |
| drawdown_mediano_%      | 44.3  |
| drawdown_95%_dei_casi_% | 60.3  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri        |
|-------:|:-----------------|
|   2021 | {"target": 10.0} |
|   2022 | {"target": 10.0} |
|   2023 | {"target": 10.0} |
|   2024 | {"target": 10.0} |
|   2025 | {"target": 10.0} |

## ultima_mezzora_gao

|                         | 0     |
|:------------------------|:------|
| trade                   | 571   |
| vincenti_%              | 46.1  |
| R_medio                 | -0.02 |
| R_totale                | -11.5 |
| profit_factor           | 0.83  |
| rendimento_%            | -11.1 |
| drawdown_max_%          | 14.4  |
| t_stat                  | -1.66 |
| anni_in_utile           | 2/5   |
| griglia_pf_sopra_1_%    | 0     |
| combinazioni            | 4     |
| drawdown_mediano_%      | 13.5  |
| drawdown_95%_dei_casi_% | 16.6  |
| supera_sviluppo         | False |

Parametri scelti nel walk-forward:

|   anno | parametri                            |
|-------:|:-------------------------------------|
|   2021 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2022 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2023 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2024 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2025 | {"segnale": "r1_e_r12", "stop": 0.5} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0     |
|:------------------------|:------|
| trade                   | 1089  |
| vincenti_%              | 23.6  |
| R_medio                 | 0.092 |
| R_totale                | 99.7  |
| profit_factor           | 1.12  |
| rendimento_%            | 103.9 |
| drawdown_max_%          | 33.3  |
| t_stat                  | 1.3   |
| anni_in_utile           | 4/5   |
| drawdown_mediano_%      | 44.3  |
| drawdown_95%_dei_casi_% | 60.3  |

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2021 | orb_zarattini {"target": 10.0} |
|   2022 | orb_zarattini {"target": 10.0} |
|   2023 | orb_zarattini {"target": 10.0} |
|   2024 | orb_zarattini {"target": 10.0} |
|   2025 | orb_zarattini {"target": 10.0} |
