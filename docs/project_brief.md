
Health EU27 Data Project – Project Brief

---------------------------------------------------------------------

1. Overview

The Health EU27 Data Project is a structured data engineering and analytics project focused on European Union health indicators.

The main objective is to clean, standardize, and harmonize multiple healthcare datasets in order to enable reliable cross-country comparisons and trend analysis.

The project uses a modular ETL pipeline to transform raw datasets into analysis-ready formats. An additional optional step generates Italian translations of processed datasets.

---------------------------------------------------------------------

2. Objectives

The project aims to:

- Standardize multiple EU health datasets
- Ensure comparability across EU27 countries
- Remove structural inconsistencies and unreliable observations
- Produce analysis-ready CSV outputs
- Provide clear documentation and a reproducible ETL workflow
- Support optional Italian translations of categorical data

---------------------------------------------------------------------

3. Datasets Included

The project integrates the following datasets:

1. Population
2. Life Expectancy
3. Health Spending
4. Mortality Causes
5. Chronic Diseases Prevalence

These datasets allow multi-dimensional analysis of demographic, healthcare, and disease-related indicators across the European Union.

---------------------------------------------------------------------

4. Key Constraints

Several constraints apply to ensure dataset consistency:

- Only EU27 countries are included
- The chronic diseases dataset is available only for the years 2014 and 2019
- Some datasets contain incomplete year coverage for certain countries
- Sweden is missing in the original health spending dataset and was reconstructed from official sources

---------------------------------------------------------------------

5. Technical Stack

The project uses a lightweight data engineering stack:

- Python
- Pandas
- Jupyter Notebook
- Modular ETL pipeline structure
- Markdown-based documentation

---------------------------------------------------------------------

6. Analytical Capabilities

The processed datasets enable:

- Cross-country health comparisons
- Gender-based analysis
- Trend analysis across multiple years
- Correlation studies between indicators
- Exploration of health spending versus outcomes
- Mortality cause distribution analysis
- Chronic disease prevalence comparisons

---------------------------------------------------------------------

7. Project Value

This project demonstrates practical data engineering and analytical skills, including:

- Real-world public data cleaning
- Multi-dataset harmonization
- Structural standardization
- Transparent documentation
- Reproducible ETL workflows