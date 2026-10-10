import pandas as pd
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"


# Load datasets
customers = pd.read_csv(RAW_DATA_PATH / "customers.csv")
accounts = pd.read_csv(RAW_DATA_PATH / "accounts.csv")
transactions = pd.read_csv(RAW_DATA_PATH / "transactions.csv")
kyc = pd.read_csv(RAW_DATA_PATH / "kyc_records.csv")
country_risk = pd.read_csv(RAW_DATA_PATH / "country_risk.csv")


# Function to inspect a dataset
def inspect_dataset(name, df):

    print("\n" + "=" * 60)
    print(f"{name.upper()}")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())


# Inspect every dataset
inspect_dataset("Customers", customers)
inspect_dataset("Accounts", accounts)
inspect_dataset("Transactions", transactions)
inspect_dataset("KYC Records", kyc)
inspect_dataset("Country Risk", country_risk)