import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"


# ============================================================
# 2. LOAD DATA
# ============================================================

customers = pd.read_csv(
    RAW_DATA_PATH / "customers.csv"
)

accounts = pd.read_csv(
    RAW_DATA_PATH / "accounts.csv"
)

transactions = pd.read_csv(
    RAW_DATA_PATH / "transactions.csv"
)

kyc = pd.read_csv(
    RAW_DATA_PATH / "kyc_records.csv"
)

country_risk = pd.read_csv(
    RAW_DATA_PATH / "country_risk.csv"
)


print("=" * 60)
print("FINSIGHT DATA VALIDATION")
print("=" * 60)


# ============================================================
# 3. CUSTOMER VALIDATION
# ============================================================

print("\nCUSTOMER VALIDATION")
print("-" * 60)

# Duplicate customer IDs
duplicate_customer_ids = customers[
    customers["customer_id"].duplicated(keep=False)
]

print(
    f"Duplicate customer IDs: "
    f"{len(duplicate_customer_ids)}"
)


# Missing emails
missing_emails = customers["email"].isna().sum()

print(
    f"Missing emails: "
    f"{missing_emails}"
)


# Missing phone numbers
missing_phones = customers["phone"].isna().sum()

print(
    f"Missing phone numbers: "
    f"{missing_phones}"
)


# Invalid ages
invalid_ages = customers[
    (customers["age"] < 18) |
    (customers["age"] > 100)
]

print(
    f"Invalid ages: "
    f"{len(invalid_ages)}"
)


# ============================================================
# 4. ACCOUNT VALIDATION
# ============================================================

print("\nACCOUNT VALIDATION")
print("-" * 60)

# Duplicate account IDs
duplicate_account_ids = accounts[
    accounts["account_id"].duplicated(keep=False)
]

print(
    f"Duplicate account IDs: "
    f"{len(duplicate_account_ids)}"
)


# Accounts with customers that don't exist
invalid_account_customers = accounts[
    ~accounts["customer_id"].isin(
        customers["customer_id"]
    )
]

print(
    f"Accounts with invalid customer IDs: "
    f"{len(invalid_account_customers)}"
)


# Negative balances
negative_balances = accounts[
    accounts["balance"] < 0
]

print(
    f"Negative account balances: "
    f"{len(negative_balances)}"
)


# ============================================================
# 5. TRANSACTION VALIDATION
# ============================================================

print("\nTRANSACTION VALIDATION")
print("-" * 60)


# Duplicate transaction IDs
duplicate_transaction_ids = transactions[
    transactions["transaction_id"].duplicated(keep=False)
]

print(
    f"Duplicate transaction IDs: "
    f"{len(duplicate_transaction_ids)}"
)


# Missing transaction amounts
missing_amounts = transactions["amount"].isna().sum()

print(
    f"Missing transaction amounts: "
    f"{missing_amounts}"
)


# Negative transaction amounts
negative_amounts = transactions[
    transactions["amount"] < 0
]

print(
    f"Negative transaction amounts: "
    f"{len(negative_amounts)}"
)


# Transactions linked to accounts that don't exist
invalid_transaction_accounts = transactions[
    ~transactions["account_id"].isin(
        accounts["account_id"]
    )
]

print(
    f"Transactions with invalid account IDs: "
    f"{len(invalid_transaction_accounts)}"
)


# Valid transaction types
valid_transaction_types = [
    "Credit",
    "Debit"
]

invalid_transaction_types = transactions[
    ~transactions["transaction_type"].isin(
        valid_transaction_types
    )
]

print(
    f"Invalid transaction types: "
    f"{len(invalid_transaction_types)}"
)


# Valid transaction statuses
valid_transaction_statuses = [
    "Completed",
    "Failed",
    "Pending"
]

invalid_transaction_statuses = transactions[
    ~transactions["transaction_status"].isin(
        valid_transaction_statuses
    )
]

print(
    f"Invalid transaction statuses: "
    f"{len(invalid_transaction_statuses)}"
)


# ============================================================
# 6. KYC VALIDATION
# ============================================================

print("\nKYC VALIDATION")
print("-" * 60)


# KYC records linked to customers that don't exist
invalid_kyc_customers = kyc[
    ~kyc["customer_id"].isin(
        customers["customer_id"]
    )
]

print(
    f"KYC records with invalid customer IDs: "
    f"{len(invalid_kyc_customers)}"
)


# Convert dates temporarily for validation
kyc["verification_date"] = pd.to_datetime(
    kyc["verification_date"],
    errors="coerce"
)

kyc["expiry_date"] = pd.to_datetime(
    kyc["expiry_date"],
    errors="coerce"
)


# Expiry date before verification date
invalid_kyc_dates = kyc[
    kyc["expiry_date"] <
    kyc["verification_date"]
]

print(
    f"KYC records with invalid dates: "
    f"{len(invalid_kyc_dates)}"
)


# ============================================================
# 7. COUNTRY RISK VALIDATION
# ============================================================

print("\nCOUNTRY RISK VALIDATION")
print("-" * 60)


# Risk score should be between 0 and 100
invalid_risk_scores = country_risk[
    (country_risk["risk_score"] < 0) |
    (country_risk["risk_score"] > 100)
]

print(
    f"Invalid risk scores: "
    f"{len(invalid_risk_scores)}"
)


# ============================================================
# 8. END
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION COMPLETE")
print("=" * 60)