
-- DROP DATABASE health_data_eu_it;
CREATE DATABASE IF NOT EXISTS health_data_eu_it;
USE health_data_eu_it;

-- =========================
-- DIMENSIONS
-- =========================

CREATE TABLE dim_country (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE dim_year (
    year_id INT AUTO_INCREMENT PRIMARY KEY,
    year INT NOT NULL UNIQUE
);

CREATE TABLE dim_sex (
    sex_id INT AUTO_INCREMENT PRIMARY KEY,
    sex_code VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE dim_disease (
    disease_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL UNIQUE
);

-- =========================
-- FACT TABLES (WITH SURROGATE KEYS)
-- =========================

CREATE TABLE fact_population (
    population_fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    year_id INT NOT NULL,
    population BIGINT,
    
    CONSTRAINT fk_pop_country FOREIGN KEY (country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_pop_year FOREIGN KEY (year_id) REFERENCES dim_year(year_id),

    CONSTRAINT uq_pop UNIQUE (country_id, year_id)
);

CREATE INDEX idx_pop_country ON fact_population(country_id);
CREATE INDEX idx_pop_year ON fact_population(year_id);


CREATE TABLE fact_life_expectancy (
    life_exp_fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    year_id INT NOT NULL,
    sex_id INT NOT NULL,
    life_expectancy DECIMAL(5,2),
    
    CONSTRAINT fk_le_country FOREIGN KEY (country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_le_year FOREIGN KEY (year_id) REFERENCES dim_year(year_id),
    CONSTRAINT fk_le_sex FOREIGN KEY (sex_id) REFERENCES dim_sex(sex_id),

    CONSTRAINT uq_le UNIQUE (country_id, year_id, sex_id)
);

CREATE INDEX idx_le_country ON fact_life_expectancy(country_id);
CREATE INDEX idx_le_year ON fact_life_expectancy(year_id);
CREATE INDEX idx_le_sex ON fact_life_expectancy(sex_id);


CREATE TABLE fact_health_spending (
    spending_fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    year_id INT NOT NULL,
    health_spending DECIMAL(10,2),
    
    CONSTRAINT fk_sp_country FOREIGN KEY (country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_sp_year FOREIGN KEY (year_id) REFERENCES dim_year(year_id),

    CONSTRAINT uq_sp UNIQUE (country_id, year_id)
);

CREATE INDEX idx_sp_country ON fact_health_spending(country_id);
CREATE INDEX idx_sp_year ON fact_health_spending(year_id);


CREATE TABLE fact_mortality (
    mortality_fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    year_id INT NOT NULL,
    sex_id INT NOT NULL,
    disease_id INT NOT NULL,
    deaths INT,
    
    CONSTRAINT fk_mort_country FOREIGN KEY (country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_mort_year FOREIGN KEY (year_id) REFERENCES dim_year(year_id),
    CONSTRAINT fk_mort_sex FOREIGN KEY (sex_id) REFERENCES dim_sex(sex_id),
    CONSTRAINT fk_mort_disease FOREIGN KEY (disease_id) REFERENCES dim_disease(disease_id),

    CONSTRAINT uq_mort UNIQUE (country_id, year_id, sex_id, disease_id)
);

CREATE INDEX idx_mort_country ON fact_mortality(country_id);
CREATE INDEX idx_mort_year ON fact_mortality(year_id);
CREATE INDEX idx_mort_sex ON fact_mortality(sex_id);
CREATE INDEX idx_mort_disease ON fact_mortality(disease_id);


CREATE TABLE fact_prevalence (
    prevalence_fact_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    year_id INT NOT NULL,
    sex_id INT NOT NULL,
    disease_id INT NOT NULL,
    prevalence DECIMAL(6,2),
    
    CONSTRAINT fk_prev_country FOREIGN KEY (country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_prev_year FOREIGN KEY (year_id) REFERENCES dim_year(year_id),
    CONSTRAINT fk_prev_sex FOREIGN KEY (sex_id) REFERENCES dim_sex(sex_id),
    CONSTRAINT fk_prev_disease FOREIGN KEY (disease_id) REFERENCES dim_disease(disease_id),

    CONSTRAINT uq_prev UNIQUE (country_id, year_id, sex_id, disease_id)
);

CREATE INDEX idx_prev_country ON fact_prevalence(country_id);
CREATE INDEX idx_prev_year ON fact_prevalence(year_id);
CREATE INDEX idx_prev_sex ON fact_prevalence(sex_id);
CREATE INDEX idx_prev_disease ON fact_prevalence(disease_id);