
import pandas as pd
from pathlib import Path

# ===========================
# EU27 countries - central list
# ===========================
EU27_COUNTRIES = [
    'AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'EL', 'ES',
    'FI', 'FR', 'HR', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 'MT',
    'NL', 'PL', 'PT', 'RO', 'SI', 'SK', 'SE'
]

# ===========================
# Generic filters and helpers
# ===========================
def filter_eu_countries(df: pd.DataFrame, country_col: str = 'country') -> pd.DataFrame:
    """Keep only EU27 countries present in df"""
    return df[df[country_col].isin(EU27_COUNTRIES)].copy()

def drop_na(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Drop rows where col has NaN"""
    return df.dropna(subset=[col]).copy()

def to_int(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Convert column to int"""
    df[col] = df[col].astype(int)
    return df

def to_numeric(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Convert column to numeric"""
    df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def keep_sex(df: pd.DataFrame, sex_col: str = 'sex', keep: list = ['F', 'M']) -> pd.DataFrame:
    """Keep only specified sex categories (exclude totals)"""
    return df[df[sex_col].isin(keep)].copy()

# ===========================
# Save processed dataframe
# ===========================
def save_processed(df: pd.DataFrame, base_path: Path, subfolder: str, original_file_name: str = None, custom_name: str = None) -> Path:
    """
    Save processed dataframe to processed folder.
    """
    save_folder = base_path / subfolder
    save_folder.mkdir(parents=True, exist_ok=True)

    if custom_name:
        new_file_name = custom_name
    elif original_file_name:
        new_file_name = f"{original_file_name.replace('.csv','')}_processed.csv"
    else:
        raise ValueError("Provide either original_file_name or custom_name")

    save_path = save_folder / new_file_name
    df.to_csv(save_path, index=False, encoding='utf-8')
    print(f"Processed CSV saved: {save_path}")
    return save_path