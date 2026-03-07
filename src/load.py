
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

BASE_PATH = Path("data/processed_it")

MYSQL_USER = "YOUR_USERNAME"
MYSQL_PASSWORD = "YOUR_PASSWORD"
MYSQL_HOST = "YOUR_HOST"
MYSQL_DATABASE = "health_data_eu_it"

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
)

# ===========================
# Load all datasets
# ===========================
population = pd.read_csv(BASE_PATH / "population/population_processed_it.csv")
life = pd.read_csv(BASE_PATH / "life_expectancy/life_expectancy_processed_it.csv")
spending = pd.read_csv(BASE_PATH / "health_spending/health_spending_processed_it.csv")
mortality = pd.read_csv(BASE_PATH / "mortality_causes/mortality_causes_processed_it.csv")
prevalence = pd.read_csv(BASE_PATH / "prevalence_chronic_diseases/prevalence_chronic_diseases_processed_it.csv")

# ===========================
# Build DIMENSIONS
# ===========================
dim_country = pd.DataFrame({"country_name": pd.concat([
    population["country"], life["country"], spending["country"], mortality["country"], prevalence["country"]
]).dropna().unique()})
dim_country.to_sql("dim_country", engine, if_exists="append", index=False)

dim_year = pd.DataFrame({"year": pd.concat([
    population["year"], life["year"], spending["year"], mortality["year"], prevalence["year"]
]).dropna().unique()})
dim_year.to_sql("dim_year", engine, if_exists="append", index=False)

dim_sex = pd.DataFrame({"sex_code": pd.concat([
    life["sex"], mortality["sex"], prevalence["sex"]
]).dropna().unique()})
dim_sex.to_sql("dim_sex", engine, if_exists="append", index=False)

dim_disease = pd.DataFrame({"disease_name": pd.concat([
    mortality["disease"], prevalence["disease"]
]).dropna().unique()})
dim_disease.to_sql("dim_disease", engine, if_exists="append", index=False)

# ===========================
# Load FACT TABLES
# ===========================
# Load dims from DB
dim_country = pd.read_sql("SELECT * FROM dim_country", engine)
dim_year = pd.read_sql("SELECT * FROM dim_year", engine)
dim_sex = pd.read_sql("SELECT * FROM dim_sex", engine)
dim_disease = pd.read_sql("SELECT * FROM dim_disease", engine)

# --- Fact Population
population = population.merge(dim_country, left_on="country", right_on="country_name")
population = population.merge(dim_year, on="year")
fact_population = population[["country_id", "year_id", "population"]]
fact_population.to_sql("fact_population", engine, if_exists="append", index=False)

# --- Fact Life Expectancy
life = life.merge(dim_country, left_on="country", right_on="country_name")
life = life.merge(dim_year, on="year")
life = life.merge(dim_sex, left_on="sex", right_on="sex_code")
fact_life = life[["country_id", "year_id", "sex_id", "life_expectancy"]]
fact_life.to_sql("fact_life_expectancy", engine, if_exists="append", index=False)

# --- Fact Health Spending
spending = spending.merge(dim_country, left_on="country", right_on="country_name")
spending = spending.merge(dim_year, on="year")
fact_spending = spending[["country_id", "year_id", "health_spending"]]
fact_spending.to_sql("fact_health_spending", engine, if_exists="append", index=False)

# --- Fact Mortality
mortality = mortality.merge(dim_country, left_on="country", right_on="country_name")
mortality = mortality.merge(dim_year, on="year")
mortality = mortality.merge(dim_sex, left_on="sex", right_on="sex_code")
mortality = mortality.merge(dim_disease, left_on="disease", right_on="disease_name")
fact_mortality = mortality[["country_id", "year_id", "sex_id", "disease_id", "deaths"]]
fact_mortality.to_sql("fact_mortality", engine, if_exists="append", index=False)

# --- Fact Prevalence
prevalence = prevalence.merge(dim_country, left_on="country", right_on="country_name")
prevalence = prevalence.merge(dim_year, on="year")
prevalence = prevalence.merge(dim_sex, left_on="sex", right_on="sex_code")
prevalence = prevalence.merge(dim_disease, left_on="disease", right_on="disease_name")
fact_prevalence = prevalence[["country_id", "year_id", "sex_id", "disease_id", "prevalence"]]
fact_prevalence.to_sql("fact_prevalence", engine, if_exists="append", index=False)

print("ALL DIMENSIONS AND FACTS LOADED SUCCESSFULLY.")