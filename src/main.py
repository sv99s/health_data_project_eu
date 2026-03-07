
import pandas as pd
from pathlib import Path
from src.transform import (
    transform_population,
    transform_life_expectancy,
    transform_health_spending,
    transform_mortality_causes,
    transform_prevalence_chronic_diseases
)
from src.utils import save_processed
from src.translate_it import translate_csv_to_it
from src.config import PROCESSED_DATA_PATH

def main():
    datasets = [
        {
            "subfolder": "population",
            "file_name": "tps00001__custom_20122499_linear_2_0.csv",
            "transform_func": transform_population,
            "processed_name": "population_processed.csv"
        },
        {
            "subfolder": "life_expectancy",
            "file_name": "tps00208__custom_20079049_linear_2_0.csv",
            "transform_func": transform_life_expectancy,
            "processed_name": "life_expectancy_processed.csv"
        },
        {
            "subfolder": "health_spending",
            "file_name": "tps00207__custom_20147124_linear_2_0.csv",
            "transform_func": transform_health_spending,
            "processed_name": "health_spending_processed.csv"
        },
        {
            "subfolder": "mortality_causes",
            "file_name": "hlth_cd_aro__custom_20078924_linear_2_0.csv",
            "transform_func": transform_mortality_causes,
            "processed_name": "mortality_causes_processed.csv"
        },
        {
            "subfolder": "prevalence_chronic_diseases",
            "file_name": "hlth_ehis_cd1b__custom_20079218_linear_2_0.csv",
            "transform_func": transform_prevalence_chronic_diseases,
            "processed_name": "prevalence_chronic_diseases_processed.csv"
        }
    ]

    for ds in datasets:
        raw_path = PROCESSED_DATA_PATH.parent / "raw" / ds["subfolder"] / ds["file_name"]
        df_raw = pd.read_csv(raw_path, dtype=str)
        df_clean = ds["transform_func"](df_raw)
        processed_path = save_processed(df_clean, PROCESSED_DATA_PATH, ds["subfolder"], custom_name=ds["processed_name"])
        translate_csv_to_it(processed_path)

if __name__ == "__main__":
    main()