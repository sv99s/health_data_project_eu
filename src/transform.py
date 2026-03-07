
import pandas as pd
from pathlib import Path
from .config import PROCESSED_DATA_PATH
from .utils import filter_eu_countries, drop_na, to_int, to_numeric, keep_sex

# ===========================
# Population
# ===========================
def transform_population(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df[['geo', 'TIME_PERIOD', 'OBS_VALUE']]

    df = df.rename(columns={
        'geo': 'country',
        'TIME_PERIOD': 'year',
        'OBS_VALUE': 'population'
    })

    df = filter_eu_countries(df)
    df = to_int(df, 'year')
    df = to_numeric(df, 'population')
    df = drop_na(df, 'population')

    return df[['country', 'year', 'population']]

# ===========================
# Life Expectancy
# ===========================
def transform_life_expectancy(df: pd.DataFrame) -> pd.DataFrame:

    df = df[['geo', 'TIME_PERIOD', 'OBS_VALUE', 'sex']]

    df = df.rename(columns={
        'geo': 'country',
        'TIME_PERIOD': 'year',
        'OBS_VALUE': 'life_expectancy'
    })

    df = filter_eu_countries(df)
    df = to_int(df, 'year')
    df = to_numeric(df, 'life_expectancy')
    df = keep_sex(df)
    df = drop_na(df, 'life_expectancy')

    return df[['country', 'year', 'sex', 'life_expectancy']]

# ===========================
# Health Spending
# ===========================
def transform_health_spending(df: pd.DataFrame) -> pd.DataFrame:

    df = df[['geo', 'TIME_PERIOD', 'OBS_VALUE']]

    df = df.rename(columns={
        'geo': 'country',
        'TIME_PERIOD': 'year',
        'OBS_VALUE': 'health_spending'
    })

    df = filter_eu_countries(df)
    df = to_int(df, 'year')
    df = to_numeric(df, 'health_spending')
    df = drop_na(df, 'health_spending')

    return df[['country', 'year', 'health_spending']]

# ===========================
# Mortality Causes
# ===========================
def transform_mortality_causes(df: pd.DataFrame) -> pd.DataFrame:

    df = df[['geo', 'TIME_PERIOD', 'sex',
             'International Statistical Classification of Diseases and Related Health Problems (ICD-10)',
             'OBS_VALUE', 'resid']]
    
    df = df.rename(columns={
        'geo': 'country',
        'TIME_PERIOD': 'year',
        'International Statistical Classification of Diseases and Related Health Problems (ICD-10)': 'disease',
        'OBS_VALUE': 'deaths'
    })

    df = filter_eu_countries(df)
    df = df[df['resid'] == 'TOT_RESID']
    df = keep_sex(df)
    df = to_int(df, 'year')
    df = to_numeric(df, 'deaths')
    df = drop_na(df, 'deaths')

    return df[['country', 'year', 'sex', 'disease', 'deaths']]

# ===========================
# Chronic diseases prevalence
# ===========================
def transform_prevalence_chronic_diseases(df: pd.DataFrame) -> pd.DataFrame:

    df = df[[
        'geo',
        'TIME_PERIOD',
        'sex',
        'Health problems',
        'age',
        'c_birth',
        'freq',
        'unit',
        'OBS_VALUE',
        'OBS_FLAG'
    ]]

    df = df[df['c_birth'] == 'NAT']
    df = df[df['age'] == 'TOTAL']
    df = df[df['freq'] == 'A']
    df = df[df['unit'] == 'PC']
    df = df[df['OBS_FLAG'].isna()]

    df = df.rename(columns={
        'geo': 'country',
        'TIME_PERIOD': 'year',
        'Health problems': 'disease',
        'OBS_VALUE': 'prevalence'
    })

    df = filter_eu_countries(df, country_col='country')
    df = keep_sex(df, sex_col='sex')
    df['year'] = df['year'].astype(int)
    df['prevalence'] = pd.to_numeric(df['prevalence'], errors='coerce')
    df['disease'] = df['disease'].astype(str)
    df['sex'] = df['sex'].astype(str)
    df = drop_na(df, col='prevalence')

    return df[['country', 'year', 'sex', 'disease', 'prevalence']]

# ===========================
# Save processed dataframe
# ===========================
def save_processed(df: pd.DataFrame, original_file_name: str,
                   subfolder: str, custom_name: str = None) -> Path:
    save_folder = PROCESSED_DATA_PATH / subfolder
    save_folder.mkdir(parents=True, exist_ok=True)

    if custom_name:
        new_file_name = custom_name
    else:
        new_file_name = f"{original_file_name.replace('.csv','')}_processed.csv"

    save_path = save_folder / new_file_name
    df.to_csv(save_path, index=False, encoding='utf-8')
    print(f"Processed CSV saved: {save_path}")
    return save_path