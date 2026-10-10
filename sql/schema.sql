-- FinSight: PostgreSQL database schema
-- Tables are created in parent-to-child order.

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    gender VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(150),
    phone VARCHAR(30),
    kyc_status VARCHAR(30),
    registration_date DATE
);

CREATE TABLE country_risk (
    country VARCHAR(100) PRIMARY KEY,
    risk_level VARCHAR(30),
    risk_score NUMERIC(5,2)
);

CREATE TABLE accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) REFERENCES customers(customer_id),
    account_type VARCHAR(30),
    balance NUMERIC(15,2),
    currency VARCHAR(10),
    opened_date DATE,
    account_status VARCHAR(30)
);

CREATE TABLE transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20) REFERENCES accounts(account_id),
    transaction_date DATE,
    transaction_type VARCHAR(30),
    amount NUMERIC(15,2),
    channel VARCHAR(30),
    merchant_category VARCHAR(50),
    transaction_status VARCHAR(30),
    location VARCHAR(100)
);

CREATE TABLE kyc_records (
    kyc_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) REFERENCES customers(customer_id),
    document_type VARCHAR(30),
    document_number VARCHAR(50),
    verification_status VARCHAR(30),
    verification_date DATE,
    expiry_date DATE
);