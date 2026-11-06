# Ricerca su US500 (pubblicate_indici) - 22/10/2026 10:06

Dati 02/07/2017 - 22/10/2026; sviluppo fino al 01/04/2025. Rischio 1% a trade. Costi: Costi(punto=0.01, commissione_oncia=0.0, spread_minimo_rel=3.2550176096452685e-05, slittamento_rel=1.6275088048226343e-05)

## Sintesi

| famiglia                                    |   trade |   profit_factor |   R_medio |   t_stat | anni_in_utile   |   griglia_pf_sopra_1_% |   drawdown_95%_dei_casi_% |   combinazioni |   supera_sviluppo |
|:--------------------------------------------|--------:|----------------:|----------:|---------:|:----------------|-----------------------:|--------------------------:|---------------:|------------------:|
| orb_zarattini                               |    1331 |            0.93 |    -0.059 |    -0.93 | 3/6             |                      0 |                      86.4 |              2 |                 0 |
| ultima_mezzora_gao                          |     659 |            0.88 |    -0.017 |    -1.16 | 2/6             |                      0 |                      19.7 |              4 |                 0 |
| APPRENDIMENTO (sceglie ogni anno tra tutte) |    1331 |            0.93 |    -0.059 |    -0.93 | 3/6             |                    nan |                      86.4 |            nan |               nan |

## orb_zarattini

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1331   |
| vincenti_%              | 19.4   |
| R_medio                 | -0.059 |
| R_totale                | -77.9  |
| profit_factor           | 0.93   |
| rendimento_%            | -67.3  |
| drawdown_max_%          | 78.9   |
| t_stat                  | -0.93  |
| anni_in_utile           | 3/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 2      |
| drawdown_mediano_%      | 78.2   |
| drawdown_95%_dei_casi_% | 86.4   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri        |
|-------:|:-----------------|
|   2020 | {"target": 10.0} |
|   2021 | {"target": 10.0} |
|   2022 | {"target": 2.5}  |
|   2023 | {"target": 10.0} |
|   2024 | {"target": 10.0} |
|   2025 | {"target": 10.0} |

## ultima_mezzora_gao

|                         | 0      |
|:------------------------|:-------|
| trade                   | 659    |
| vincenti_%              | 46.1   |
| R_medio                 | -0.017 |
| R_totale                | -11.1  |
| profit_factor           | 0.88   |
| rendimento_%            | -11.0  |
| drawdown_max_%          | 18.3   |
| t_stat                  | -1.16  |
| anni_in_utile           | 2/6    |
| griglia_pf_sopra_1_%    | 0      |
| combinazioni            | 4      |
| drawdown_mediano_%      | 15.2   |
| drawdown_95%_dei_casi_% | 19.7   |
| supera_sviluppo         | False  |

Parametri scelti nel walk-forward:

|   anno | parametri                            |
|-------:|:-------------------------------------|
|   2020 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2021 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2022 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2023 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2024 | {"segnale": "r1_e_r12", "stop": 0.5} |
|   2025 | {"segnale": "r1_e_r12", "stop": 0.5} |

## Apprendimento: ogni anno sceglie tra tutte le combinazioni

|                         | 0      |
|:------------------------|:-------|
| trade                   | 1331   |
| vincenti_%              | 19.4   |
| R_medio                 | -0.059 |
| R_totale                | -77.9  |
| profit_factor           | 0.93   |
| rendimento_%            | -67.3  |
| drawdown_max_%          | 78.9   |
| t_stat                  | -0.93  |
| anni_in_utile           | 3/6    |
| drawdown_mediano_%      | 78.2   |
| drawdown_95%_dei_casi_% | 86.4   |

|   anno | parametri                      |
|-------:|:-------------------------------|
|   2020 | orb_zarattini {"target": 10.0} |
|   2021 | orb_zarattini {"target": 10.0} |
|   2022 | orb_zarattini {"target": 2.5}  |
|   2023 | orb_zarattini {"target": 10.0} |
|   2024 | orb_zarattini {"target": 10.0} |
|   2025 | orb_zarattini {"target": 10.0} |
