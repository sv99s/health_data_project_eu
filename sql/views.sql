SELECT * FROM dim_country;
SELECT * FROM dim_year;
SELECT * FROM dim_sex;
SELECT * FROM dim_disease;

SELECT * FROM fact_health_spending;
SELECT * FROM fact_life_expectancy;
SELECT * FROM fact_mortality;
SELECT * FROM fact_population;
SELECT * FROM fact_prevalence;

NEW COLUMN:
Mortality Diseases = 
DISTINCT (
    SELECTCOLUMNS (
        'health_data_eu_it fact_mortality',
        "disease_id", 'health_data_eu_it fact_mortality'[disease_id],
        "disease_name", RELATED('health_data_eu_it dim_disease'[disease_name])
    )
)

DAX:
mortality_rate_percentage = 
VAR TotalDeaths =
    SUM('health_data_eu_it fact_mortality'[deaths])
VAR CountryPopulation =
    CALCULATE(
        SUM('health_data_eu_it fact_population'[population]),
        TREATAS(
            VALUES('health_data_eu_it dim_country'[country_id]),
            'health_data_eu_it fact_population'[country_id]
        ),
        TREATAS(
            VALUES('health_data_eu_it dim_year'[year_id]),
            'health_data_eu_it fact_population'[year_id]
        )
    )
RETURN
IF(
    NOT(ISBLANK(CountryPopulation)) && CountryPopulation > 0,
    DIVIDE(TotalDeaths, CountryPopulation, 0) * 100,
    BLANK()
)