
This document describes the structure, meaning, and standardization of all processed datasets used in the Health_Care_Project.

All datasets were cleaned, filtered to EU27 countries, and standardized for analytical consistency.

---------------------------------------------------------------------

1. Population Dataset

Processed File: population_processed.csv

Column        Type       Description
------------  ---------  ----------------------------------
country       string     ISO country code (EU27 only)
year          integer    Reference year
population    integer    Total population

Notes:
- Non-EU and aggregated entities removed.
- Missing values removed.
- Year range: 2014 – 2025.

---------------------------------------------------------------------

2. Life Expectancy Dataset

Processed File: life_expectancy_processed.csv

Column           Type       Description
---------------  ---------  -----------------------------------------
country          string     ISO country code (EU27 only)
year             integer    Reference year
sex              string     F (female) / M (male)
life_expectancy  float      Life expectancy at birth (years)

Notes:
- Non-EU and aggregated entities removed.
- Missing values removed.
- Year range: 2012 – 2023.

---------------------------------------------------------------------

3. Health Spending Dataset

Processed File: health_spending_processed.csv

Column           Type       Description
---------------  ---------  -----------------------------------
country          string     ISO country code (EU27 only)
year             integer    Reference year
health_spending  float      Health expenditure indicator per person

Notes:
- Non-EU and aggregated entities removed.
- Sweden (SE) not present in original dataset.
- Missing numeric values removed.

---------------------------------------------------------------------

4. Mortality Causes Dataset

Processed File: mortality_causes_processed.csv

Column          Type       Description
--------------  ---------  -----------------------------------------
country         string     ISO country code (EU27 only)
year            integer    Reference year
sex             string     F / M
disease         string     Cause of death
deaths          float      Mortality rate indicator

Notes:
- Non-EU and aggregated entities removed.
- Missing values removed.

---------------------------------------------------------------------

5. Chronic Diseases Prevalence Dataset

Processed File: prevalence_chronic_diseases_processed.csv

Column      Type       Description
----------  ---------  ------------------------------------------
country     string     ISO country code (EU27 only)
year        integer    Reference year
sex         string     F / M
disease     string     Health problem (disease name)
prevalence  float      Percentage of population affected

Notes:
- Non-EU and aggregated entities removed.
- Dataset contains data only for years 2014 and 2019.
- Missing values removed.

---------------------------------------------------------------------

General Standardization Rules

All processed datasets follow these conventions:

- EU27 countries only
- Missing values removed
- Column names standardized to snake_case
- Consistent country and year structure across datasets
- Italian translations stored in data/processed_it/

This ensures cross-dataset compatibility and analytical consistency.