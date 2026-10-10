import pandas as pd
import numpy as np
import random
from pathlib import Path
from datetime import datetime, timedelta


# ============================================================
# 1. PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. SETTINGS
# ============================================================

random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 2000
NUM_ACCOUNTS = 3000
NUM_TRANSACTIONS = 50000


# ============================================================
# 3. CUSTOMER DATA
# ============================================================

first_names = [
    "Rahul", "Ankit", "Priya", "Sneha", "Arjun",
    "Vikram", "Neha", "Rohan", "Amit", "Kavya",
    "Aditya", "Pooja", "Nikhil", "Meera", "Karan"
]

last_names = [
    "Sharma", "Patel", "Kumar", "Singh", "Verma",
    "Reddy", "Nair", "Iyer", "Mehta", "Joshi"
]

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad"
]

countries = [
    "India",
    "USA",
    "UK",
    "Singapore",
    "UAE",
    "Germany"
]

genders = ["M", "F"]

kyc_statuses = [
    "Verified",
    "Pending",
    "Rejected"
]

customers = []

start_date = datetime(2022, 1, 1)

for i in range(1, NUM_CUSTOMERS + 1):

    first = random.choice(first_names)
    last = random.choice(last_names)

    customer_id = f"C{i:04d}"

    registration_date = (
        start_date +
        timedelta(days=random.randint(0, 1700))
    )

    customers.append({
        "customer_id": customer_id,
        "name": f"{first} {last}",
        "age": random.randint(21, 65),
        "gender": random.choice(genders),
        "city": random.choice(cities),
        "country": random.choice(countries),
        "email": f"{first.lower()}.{last.lower()}{i}@example.com",
        "phone": str(random.randint(6000000000, 9999999999)),
        "kyc_status": random.choice(kyc_statuses),
        "registration_date": registration_date.strftime("%Y-%m-%d")
    })


customers_df = pd.DataFrame(customers)


# ============================================================
# 4. INTRODUCE CUSTOMER DATA QUALITY ISSUES
# ============================================================

# Inconsistent city capitalization
customers_df.loc[10, "city"] = "bangalore"
customers_df.loc[25, "city"] = "BANGALORE"
customers_df.loc[50, "city"] = "bengaluru"

# Missing email
customers_df.loc[100, "email"] = np.nan

# Missing phone
customers_df.loc[150, "phone"] = np.nan

# Duplicate customer
duplicate_customer = customers_df.iloc[[200]].copy()
customers_df = pd.concat(
    [customers_df, duplicate_customer],
    ignore_index=True
)


# ============================================================
# 5. ACCOUNT DATA
# ============================================================

account_types = [
    "Savings",
    "Current",
    "Salary"
]

account_statuses = [
    "Active",
    "Inactive",
    "Frozen"
]

accounts = []

for i in range(1, NUM_ACCOUNTS + 1):

    customer_id = random.choice(
        customers_df["customer_id"].drop_duplicates().tolist()
    )

    accounts.append({
        "account_id": f"A{i:05d}",
        "customer_id": customer_id,
        "account_type": random.choice(account_types),
        "balance": round(random.uniform(5000, 2000000), 2),
        "currency": "INR",
        "opened_date": (
            start_date +
            timedelta(days=random.randint(0, 1500))
        ).strftime("%Y-%m-%d"),
        "account_status": random.choice(account_statuses)
    })


accounts_df = pd.DataFrame(accounts)


# ============================================================
# 6. TRANSACTION DATA
# ============================================================

transaction_types = [
    "Credit",
    "Debit"
]

channels = [
    "ATM",
    "Online",
    "Branch",
    "Mobile"
]

merchant_categories = [
    "Salary",
    "Shopping",
    "Food",
    "Travel",
    "Utilities",
    "Cash Withdrawal",
    "Investment",
    "Transfer"
]

transaction_statuses = [
    "Completed",
    "Failed",
    "Pending"
]

locations = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

account_ids = accounts_df["account_id"].tolist()

transactions = []

transaction_start = datetime(2025, 1, 1)

for i in range(1, NUM_TRANSACTIONS + 1):

    transactions.append({
        "transaction_id": f"T{i:06d}",
        "account_id": random.choice(account_ids),
        "transaction_date": (
            transaction_start +
            timedelta(days=random.randint(0, 639))
        ).strftime("%Y-%m-%d"),
        "transaction_type": random.choice(transaction_types),
        "amount": round(random.uniform(100, 1000000), 2),
        "channel": random.choice(channels),
        "merchant_category": random.choice(merchant_categories),
        "transaction_status": random.choice(transaction_statuses),
        "location": random.choice(locations)
    })


transactions_df = pd.DataFrame(transactions)


# ============================================================
# 7. INTRODUCE TRANSACTION DATA QUALITY ISSUES
# ============================================================

# Missing amount
transactions_df.loc[100, "amount"] = np.nan

# Invalid negative amount
transactions_df.loc[200, "amount"] = -5000

# Invalid account reference
transactions_df.loc[300, "account_id"] = "A99999"

# Duplicate transaction
duplicate_transaction = transactions_df.iloc[[400]].copy()
transactions_df = pd.concat(
    [transactions_df, duplicate_transaction],
    ignore_index=True
)


# ============================================================
# 8. KYC DATA
# ============================================================

document_types = [
    "PAN",
    "Passport",
    "Driving License",
    "Aadhaar"
]

verification_statuses = [
    "Verified",
    "Pending",
    "Rejected"
]

kyc_records = []

for i, customer_id in enumerate(
    customers_df["customer_id"].drop_duplicates(),
    start=1
):

    verification_date = datetime(2024, 1, 1) + timedelta(
        days=random.randint(0, 1000)
    )

    expiry_date = verification_date + timedelta(
        days=random.choice([365, 730, 1095])
    )

    kyc_records.append({
        "kyc_id": f"K{i:05d}",
        "customer_id": customer_id,
        "document_type": random.choice(document_types),
        "document_number": f"DOC{i:07d}",
        "verification_status": random.choice(
            verification_statuses
        ),
        "verification_date": verification_date.strftime("%Y-%m-%d"),
        "expiry_date": expiry_date.strftime("%Y-%m-%d")
    })


kyc_df = pd.DataFrame(kyc_records)


# Introduce missing KYC record by removing one customer
kyc_df = kyc_df.iloc[:-10]


# ============================================================
# 9. COUNTRY RISK DATA
# ============================================================

country_risk_data = [
    ["India", "Low", 20],
    ["USA", "Low", 15],
    ["UK", "Low", 15],
    ["Singapore", "Low", 10],
    ["UAE", "Medium", 45],
    ["Germany", "Low", 15],
    ["Country_X", "High", 90],
    ["Country_Y", "High", 85],
    ["Country_Z", "Medium", 60],
    ["Country_A", "Medium", 55]
]

country_risk_df = pd.DataFrame(
    country_risk_data,
    columns=[
        "country",
        "risk_level",
        "risk_score"
    ]
)


# ============================================================
# 10. SAVE RAW DATA
# ============================================================

customers_df.to_csv(
    RAW_DATA_PATH / "customers.csv",
    index=False
)

accounts_df.to_csv(
    RAW_DATA_PATH / "accounts.csv",
    index=False
)

transactions_df.to_csv(
    RAW_DATA_PATH / "transactions.csv",
    index=False
)

kyc_df.to_csv(
    RAW_DATA_PATH / "kyc_records.csv",
    index=False
)

country_risk_df.to_csv(
    RAW_DATA_PATH / "country_risk.csv",
    index=False
)


# ============================================================
# 11. DISPLAY SUMMARY
# ============================================================

print("\n======================================")
print("FinSight Raw Data Generation Complete")
print("======================================")

print(f"Customers:     {len(customers_df):,}")
print(f"Accounts:      {len(accounts_df):,}")
print(f"Transactions:  {len(transactions_df):,}")
print(f"KYC Records:   {len(kyc_df):,}")
print(f"Country Risk:  {len(country_risk_df):,}")

print("\nFiles saved to:")
print(RAW_DATA_PATH)