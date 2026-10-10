import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD RAW DATA
# ============================================================

customers = pd.read_csv(RAW_DATA_PATH / "customers.csv")
accounts = pd.read_csv(RAW_DATA_PATH / "accounts.csv")
transactions = pd.read_csv(RAW_DATA_PATH / "transactions.csv")
kyc = pd.read_csv(RAW_DATA_PATH / "kyc_records.csv")
country_risk = pd.read_csv(RAW_DATA_PATH / "country_risk.csv")


print("=" * 60)
print("FINSIGHT DATA CLEANING")
print("=" * 60)

print("\nRaw data loaded successfully.")

print(f"Customers: {len(customers):,}")
print(f"Accounts: {len(accounts):,}")
print(f"Transactions: {len(transactions):,}")
print(f"KYC Records: {len(kyc):,}")
print(f"Country Risk: {len(country_risk):,}")
# ============================================================
# 3. CLEAN CUSTOMERS
# ============================================================

print("\nCleaning customers...")

# Remove duplicate customer IDs
customers = customers.drop_duplicates(
    subset="customer_id",
    keep="first"
)

# Replace missing emails with a standard value
customers["email"] = customers["email"].fillna("Not Available")

# Replace missing phone numbers with a standard value
customers["phone"] = customers["phone"].fillna("Not Available")

# Convert registration date to proper datetime format
customers["registration_date"] = pd.to_datetime(
    customers["registration_date"],
    errors="coerce"
)

print(f"Customers after cleaning: {len(customers):,}")
print(f"Duplicate customer IDs remaining: {customers['customer_id'].duplicated().sum()}")
print(f"Missing emails remaining: {customers['email'].isna().sum()}")
print(f"Missing phone numbers remaining: {customers['phone'].isna().sum()}")

# ============================================================
# 4. CLEAN ACCOUNTS
# ============================================================

print("\nCleaning accounts...")

# Remove duplicate account IDs
accounts = accounts.drop_duplicates(
    subset="account_id",
    keep="first"
)

# Convert balance to numeric
accounts["balance"] = pd.to_numeric(
    accounts["balance"],
    errors="coerce"
)

# Convert opened date to proper datetime
accounts["opened_date"] = pd.to_datetime(
    accounts["opened_date"],
    errors="coerce"
)

# Standardize text columns
accounts["account_type"] = accounts["account_type"].str.strip()
accounts["currency"] = accounts["currency"].str.strip()
accounts["account_status"] = accounts["account_status"].str.strip()

print(f"Accounts after cleaning: {len(accounts):,}")
print(f"Duplicate account IDs remaining: {accounts['account_id'].duplicated().sum()}")
print(f"Missing balances: {accounts['balance'].isna().sum()}")
print(f"Invalid opened dates: {accounts['opened_date'].isna().sum()}")
# ============================================================
# 5. CLEAN TRANSACTIONS
# ============================================================

print("\nCleaning transactions...")

# Remove duplicate transaction IDs
transactions = transactions.drop_duplicates(
    subset="transaction_id",
    keep="first"
)

# Convert amount to numeric
transactions["amount"] = pd.to_numeric(
    transactions["amount"],
    errors="coerce"
)

# Remove transactions with missing amounts
transactions = transactions.dropna(
    subset=["amount"]
)

# Remove transactions with negative amounts
transactions = transactions[
    transactions["amount"] > 0
]

# Keep only transactions whose account exists
transactions = transactions[
    transactions["account_id"].isin(
        accounts["account_id"]
    )
]

# Convert transaction date to proper datetime
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

# Remove transactions with invalid dates
transactions = transactions.dropna(
    subset=["transaction_date"]
)

# Standardize text columns
transactions["transaction_type"] = (
    transactions["transaction_type"].str.strip()
)

transactions["channel"] = (
    transactions["channel"].str.strip()
)

transactions["merchant_category"] = (
    transactions["merchant_category"].str.strip()
)

transactions["transaction_status"] = (
    transactions["transaction_status"].str.strip()
)

transactions["location"] = (
    transactions["location"].str.strip()
)


print(
    f"Transactions after cleaning: "
    f"{len(transactions):,}"
)

print(
    f"Duplicate transaction IDs remaining: "
    f"{transactions['transaction_id'].duplicated().sum()}"
)

print(
    f"Missing transaction amounts remaining: "
    f"{transactions['amount'].isna().sum()}"
)

print(
    f"Negative transaction amounts remaining: "
    f"{(transactions['amount'] < 0).sum()}"
)

print(
    f"Invalid account IDs remaining: "
    f"{(~transactions['account_id'].isin(accounts['account_id'])).sum()}"
)

print(
    f"Invalid transaction dates remaining: "
    f"{transactions['transaction_date'].isna().sum()}"
)
# ============================================================
# 6. CLEAN KYC
# ============================================================

print("\nCleaning KYC records...")

# Remove duplicate KYC IDs
kyc = kyc.drop_duplicates(
    subset="kyc_id",
    keep="first"
)

# Keep only KYC records belonging to valid customers
kyc = kyc[
    kyc["customer_id"].isin(
        customers["customer_id"]
    )
]

# Convert dates to proper datetime format
kyc["verification_date"] = pd.to_datetime(
    kyc["verification_date"],
    errors="coerce"
)

kyc["expiry_date"] = pd.to_datetime(
    kyc["expiry_date"],
    errors="coerce"
)

# Remove records with invalid dates
kyc = kyc.dropna(
    subset=[
        "verification_date",
        "expiry_date"
    ]
)

# Standardize text columns
kyc["document_type"] = (
    kyc["document_type"].str.strip()
)

kyc["document_number"] = (
    kyc["document_number"].str.strip()
)

kyc["verification_status"] = (
    kyc["verification_status"].str.strip()
)

print(
    f"KYC records after cleaning: "
    f"{len(kyc):,}"
)

print(
    f"Duplicate KYC IDs remaining: "
    f"{kyc['kyc_id'].duplicated().sum()}"
)

print(
    f"Invalid customer IDs remaining: "
    f"{(~kyc['customer_id'].isin(customers['customer_id'])).sum()}"
)

print(
    f"Invalid verification dates: "
    f"{kyc['verification_date'].isna().sum()}"
)

print(
    f"Invalid expiry dates: "
    f"{kyc['expiry_date'].isna().sum()}"
)
# ============================================================
# 7. CLEAN COUNTRY RISK
# ============================================================

print("\nCleaning country risk data...")

# Remove duplicate countries
country_risk = country_risk.drop_duplicates(
    subset="country",
    keep="first"
)

# Standardize text columns
country_risk["country"] = (
    country_risk["country"].str.strip()
)

country_risk["risk_level"] = (
    country_risk["risk_level"].str.strip()
)

# Convert risk score to numeric
country_risk["risk_score"] = pd.to_numeric(
    country_risk["risk_score"],
    errors="coerce"
)

# Remove records with missing risk scores
country_risk = country_risk.dropna(
    subset=["risk_score"]
)

# Keep risk scores within a valid range
country_risk = country_risk[
    country_risk["risk_score"].between(0, 100)
]

print(
    f"Country risk records after cleaning: "
    f"{len(country_risk):,}"
)

print(
    f"Duplicate countries remaining: "
    f"{country_risk['country'].duplicated().sum()}"
)

print(
    f"Missing risk scores remaining: "
    f"{country_risk['risk_score'].isna().sum()}"
)

print(
    f"Invalid risk scores remaining: "
    f"{((country_risk['risk_score'] < 0) | (country_risk['risk_score'] > 100)).sum()}"
)
# ============================================================
# 8. SAVE PROCESSED DATA
# ============================================================

print("\nSaving processed data...")

customers.to_csv(
    PROCESSED_DATA_PATH / "customers_clean.csv",
    index=False
)

accounts.to_csv(
    PROCESSED_DATA_PATH / "accounts_clean.csv",
    index=False
)

transactions.to_csv(
    PROCESSED_DATA_PATH / "transactions_clean.csv",
    index=False
)

kyc.to_csv(
    PROCESSED_DATA_PATH / "kyc_records_clean.csv",
    index=False
)

country_risk.to_csv(
    PROCESSED_DATA_PATH / "country_risk_clean.csv",
    index=False
)

print("Processed datasets saved successfully.")