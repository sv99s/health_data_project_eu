
# ⚠️ Note on Population Data:
# - Population data for France and Czechia (2014–2025) were missing in the original Eurostat sources.
# - These values have been added manually to the `population_processed_it.csv` file.
# - Sources used for these data:
#     • France: INSEE (National Institute of Statistics and Economic Studies) – https://www.insee.fr/en/statistiques
#     • Czechia: Czech Statistical Office – https://www.czso.cz/csu/czso/home

import pandas as pd

input_csv = "data/processed_it/population/population_processed_it.csv"
df_existing = pd.read_csv(input_csv)

new_data = [
    ("Francia", 2014, 66130000),
    ("Francia", 2015, 66420000),
    ("Francia", 2016, 66600000),
    ("Francia", 2017, 66770000),
    ("Francia", 2018, 66990000),
    ("Francia", 2019, 67260000),
    ("Francia", 2020, 67420000),
    ("Francia", 2021, 67640000),
    ("Francia", 2022, 67830000),
    ("Francia", 2023, 68040000),
    ("Francia", 2024, 68260000),
    ("Francia", 2025, 69080000),
    
    ("Repubblica Ceca", 2014, 10500000),
    ("Repubblica Ceca", 2015, 10520000),
    ("Repubblica Ceca", 2016, 10540000),
    ("Repubblica Ceca", 2017, 10560000),
    ("Repubblica Ceca", 2018, 10590000),
    ("Repubblica Ceca", 2019, 10610000),
    ("Repubblica Ceca", 2020, 10697000),
    ("Repubblica Ceca", 2021, 10706000),
    ("Repubblica Ceca", 2022, 10702000),
    ("Repubblica Ceca", 2023, 10660000),
    ("Repubblica Ceca", 2024, 10650000),
    ("Repubblica Ceca", 2025, 10640000),
]

df_new = pd.DataFrame(new_data, columns=["country", "year", "population"])

df_combined = pd.concat([df_existing, df_new], ignore_index=True)

df_combined.to_csv(input_csv, index=False)