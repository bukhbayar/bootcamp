{{ config(
    materialized='incremental',
    incremental_strategy='append',
    unique_key='transaction_id',
    on_schema_change='sync_all_columns'
) }}


SELECT
    t.transaction_id,
    t.account_id,
    a.customer_code,
    t.bank_name,
    t.transaction_type,
    t.amount,
    t.currency,
    t.transaction_date,
    t.status,
    t.description,
    t.merchant_name,
    t.reference,
    t.transaction_category
FROM {{ ref('stg_transactions') }} t
LEFT JOIN {{ ref('stg_accounts') }} a ON a.account_number = t.account_id