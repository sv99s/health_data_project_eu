
This document summarizes the main issues and observations identified in the datasets of the **Health EU27 Data Project**. The goal is to provide clarity and context for users or developers who will analyze or use these datasets.

---

## 1. Life Expectancy Dataset

- **File:** `tps00208__custom_20079049_linear_2_0.csv`
- **Observations:**
  - Row counts per country and sex vary slightly; some countries have incomplete years:
    - Example: `MT` only 12 rows.

---

## 2. Health Spending Dataset

- **File:** `tps00207__custom_20147124_linear_2_0.csv`
- **Observations:**
  - The dataset contains 26 out of the 27 EU countries; Sweden (`SE`) is missing.
  - The number of observations differs slightly between countries (some countries have fewer years available):
    - Example: `MT` 10 years, `SK` 11 years.
- **Actions:** 
  - The missing data for Sweden was manually added using official statistics, with AI assistance, based on data from:
  - Eurostat: https://ec.europa.eu/eurostat
  - OECD Health Statistics: https://stats.oecd.org/

---

## 3. Chronic Diseases Prevalence Dataset

- **File:** `hlth_ehis_cd1b__custom_20079218_linear_2_0.csv`
- **Observations:**
  - Some records are marked with low reliability (`OBS_FLAG = 'u'`).
  - The dataset contains data only for the years 2014 and 2019.
- **Actions:**
  - Removed all records with non-null `OBS_FLAG` (low reliability values).

---

## 4. Population Dataset

- **File:** `tps00001__custom_20122499_linear_2_0.csv`
- **Observations:**
- Population data for France and Czechia (2014–2025) were missing in the original Eurostat sources.
- **Actions:**
- These values have been manually added using the script `src/add_missing_population_it.py`.
- France: INSEE – https://www.insee.fr/en/statistiques
- Czechia: Czech Statistical Office – https://www.czso.cz/csu/czso/home

---

## 5. General Observations

- Different CSV files may include aggregated or non-EU entities; therefore, manual filtering is required during transformation.
- Some datasets have incomplete year coverage for certain countries.
- The Chronic Diseases dataset has limited temporal coverage (2014 and 2019 only), which restricts longitudinal analysis.
- Structural dimensions differ significantly across datasets, making automatic validation impractical.
- All datasets were standardized to a clean analytical structure during transformation.
- Italian translations are stored in `data/processed_it/`.
- It is recommended to use a separate Jupyter Notebook (`visualization.ipynb`) for quick validation, visual checks, and anomaly detection.