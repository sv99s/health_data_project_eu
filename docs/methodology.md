
Health EU27 Data Project – ETL Overview

This document summarizes the ETL pipeline used in the Health EU27 Data Project.

---------------------------------------------------------------------

1. Project Structure

The project follows a modular ETL pipeline:

1. Transform raw CSV datasets
2. Optional translation to Italian
3. Load processed datasets into MySQL
4. Visualization and exploratory analysis

Raw data:        /data/raw/
Processed data:  /data/processed/
Italian data:    /data/processed_it/

---------------------------------------------------------------------

2. Data Extraction

Raw datasets are stored as CSV files in /data/raw/.
Extraction is performed directly in main.py using pandas read_csv().

No separate extract module is used.

---------------------------------------------------------------------

3. Data Transformation

All datasets undergo basic cleaning and standardization before analysis.

Typical transformation steps:

- Keep EU27 countries only
- Standardize column names (country, year, etc.)
- Remove rows with missing or invalid values
- Filter specific variables when necessary (age, unit, reliability flags)

Processed datasets include:

- Population
- Life Expectancy
- Health Spending
- Mortality Causes
- Chronic Disease Prevalence

Clean datasets are saved in /data/processed/.

---------------------------------------------------------------------

4. Italian Translation

Categorical fields can optionally be translated to Italian.

Handled by:
src/translate_it.py

Only text fields are translated (disease names, country names).
Numeric values remain unchanged.

Translated datasets are saved in /data/processed_it/.

---------------------------------------------------------------------

5. Loading into MySQL

Processed CSV datasets can be loaded into MySQL databases.

Key characteristics:
- Standardized table structures
- Consistent data types
- No index columns exported

Used database:
health_data_eu_it

---------------------------------------------------------------------

6. Validation

Basic validation checks include:

- Missing value verification
- EU27 country filtering
- Year range consistency
- Numeric value validation
- Basic distribution checks

---------------------------------------------------------------------

7. Design Principles

The ETL pipeline was designed with the following goals:

- Reproducibility
- Modularity
- Transparency
- Analytical consistency
- Maintainability
- Easy extension for new datasets