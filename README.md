# FinSight — Financial Data Intelligence & ETL Pipeline

## Overview

FinSight is an end-to-end financial data analytics project built to demonstrate data ingestion, data quality validation, cleaning, relational database management, SQL analysis, and interactive business intelligence reporting.

The project uses synthetic financial data to explore customer accounts, transactions, KYC verification, and country risk.

## Business Objectives

- Build a repeatable ETL workflow for financial datasets.
- Identify missing values, duplicate records, and invalid data.
- Store cleaned data in a relational PostgreSQL database.
- Perform analytical queries using SQL.
- Develop a multi-page Power BI dashboard to support data-driven decisions.

## Technology Stack

- **Python:** Data generation, inspection, validation, and cleaning
- **Pandas:** Data transformation and quality checks
- **PostgreSQL:** Relational data storage and SQL analysis
- **SQL:** Joins, aggregations, and analytical queries
- **Power BI:** Interactive dashboards and KPI reporting
- **Git and GitHub:** Version control and project sharing

## Data Sources

This project uses synthetic datasets generated for demonstration purposes.

| Dataset | Description |
|---|---|
| Customers | Customer profile and registration information |
| Accounts | Account types, balances, and status |
| Transactions | Transaction amounts, dates, types, and channels |
| KYC Records | Document verification and expiry information |
| Country Risk | Country-level risk classifications and scores |

## ETL Workflow

1. **Extract:** Generate and load raw CSV datasets.
2. **Inspect:** Examine data structure, data types, missing values, and duplicates.
3. **Validate:** Check identifiers, relationships, numeric values, and business rules.
4. **Transform:** Clean duplicates, handle missing values, remove invalid transactions, and standardize fields.
5. **Load:** Import the cleaned datasets into PostgreSQL tables.
6. **Analyze:** Query the relational data using SQL.
7. **Visualize:** Build interactive Power BI reports.

## Power BI Dashboard

The dashboard contains four pages:

1. **Executive Overview** — Key business performance indicators.
2. **Transaction Analysis** — Transaction trends and category-level analysis.
3. **Customer & Account Analysis** — Customer distribution and account insights.
4. **Risk & KYC Analysis** — KYC verification status, expiry trends, and country risk scores.

## Project Structure

```text
FinSight/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── powerbi/
├── sql/
├── src/
│   ├── generate_data.py
│   ├── inspect_data.py
│   ├── validate_raw_data.py
│   └── clean_data.py
└── README.md
```

## Running the Python Pipeline

Install the required dependency:

```bash
pip install pandas
```

Run the scripts from the project root:

```bash
python src/generate_data.py
python src/inspect_data.py
python src/validate_raw_data.py
python src/clean_data.py
```

The cleaning script generates processed CSV files for database loading.

## Database

Create a PostgreSQL database named `finsight`, then create and populate the tables using the SQL schema and cleaned CSV files.

The database contains customers, accounts, transactions, KYC records, and country risk tables.

## Key Learning Outcomes

- Building a multi-step ETL pipeline
- Applying data-quality validation rules
- Designing relational tables with primary and foreign keys
- Writing SQL joins and aggregation queries
- Developing interactive Power BI reports
- Connecting Python, PostgreSQL, SQL, and Power BI in one workflow

## Disclaimer

FinSight is an educational portfolio project. All generated financial and customer records are synthetic and do not represent real customers or transactions.