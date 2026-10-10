-- 1. Top 10 customers by total transaction value
SELECT
    c.customer_id,
    c.name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_transaction_value
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY c.customer_id, c.name
ORDER BY total_transaction_value DESC
LIMIT 10;


-- 2. Transaction value by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_value,
    AVG(amount) AS average_value
FROM transactions
GROUP BY transaction_type
ORDER BY total_value DESC;


-- 3. Monthly transaction trends
SELECT
    DATE_TRUNC('month', transaction_date)::DATE AS transaction_month,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_transaction_value
FROM transactions
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY transaction_month;


-- 4. KYC verification status distribution
SELECT
    verification_status,
    COUNT(*) AS record_count
FROM kyc_records
GROUP BY verification_status
ORDER BY record_count DESC;


-- 5. Average country risk score
SELECT
    country,
    risk_level,
    risk_score
FROM country_risk
ORDER BY risk_score DESC;


-- 6. Customers without an account
SELECT
    c.customer_id,
    c.name
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;


-- 7. Accounts with no transactions
SELECT
    a.account_id,
    a.customer_id,
    a.account_type,
    a.balance
FROM accounts a
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;