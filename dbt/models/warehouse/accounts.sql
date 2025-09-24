{{ config(
    materialized='incremental',
    incremental_strategy='append',
    unique_key='account_pk',
    on_schema_change='sync_all_columns'
) }}

WITH accounts AS (
    SELECT
        account_id,
        account_number,
        customer_code,
        bank_name,
        branch_name,
        bank_code,
        swift_code,
        account_type,
        opening_date,
        balance,
        account_status,
        interest_rate,
        currency,
        CAST('{{ var("load_date") }}' AS DATE) AS load_date
    FROM
        {{ ref('stg_accounts') }}
)


SELECT
    {{ dbt_utils.generate_surrogate_key(['account_id', 'load_date']) }} AS account_pk,
    account_id,
    account_number,
    customer_code,
    bank_name,
    branch_name,
    bank_code,
    swift_code,
    account_type,
    opening_date,
    balance,
    account_status,
    interest_rate,
    currency,
    load_date
FROM accounts a
