{{ config(
    materialized='table'
) }}

SELECT
  CONCAT(account_id, customer_id) AS account_id,
  account_id AS account_number,
  customer_id AS customer_code,
  bank_name,
  branch_name,
  bank_code,
  swift_code,
  account_type,
  opening_date,
  balance,
  status AS account_status,
  interest_rate,
  currency
FROM
    {{ source('raw', 'accounts') }} c