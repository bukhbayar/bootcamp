{{ config(
    materialized='table'
) }}

SELECT
    transaction_id,
    account_id,
    bank_name,
    transaction_type,
    amount,
    currency,
    transaction_date,
    status,
    description,
    merchant_name,
    reference,
    transaction_category
FROM
    {{ source('raw', 'transactions') }} t
WHERE
    date(t.transaction_date) = '{{ var("load_date") }}'
