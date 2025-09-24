{{ config(
    materialized='table'
) }}


with dedup_customer as (
    -- This CTE is intended to deduplicate customer records based on customer_code
    SELECT
      c.*,
      RANK() OVER (PARTITION BY customer_code ORDER BY id_number DESC) as customer_rank
    FROM
        {{ source('raw', 'customers') }} c
),

stg_customers as (
    SELECT
        customer_code,
        first_name,
        last_name,
        id_number,
        date_of_birth,
        gender,
        email,
        phone_number,
        province,
        city,
        postal_code,
        income_bracket,
        employment_status,
        credit_score,
        primary_bank,
        primary_branch
    FROM
        dedup_customer
    WHERE
        customer_rank = 1
    --     AND customer_code!='CUS10007'

    -- UNION ALL

    -- SELECT
    --     customer_code,
    --     'Customer' AS first_name,
    --     last_name,
    --     id_number,
    --     date_of_birth,
    --     gender,
    --     email,
    --     phone_number,
    --     province,
    --     city,
    --     postal_code,
    --     income_bracket,
    --     employment_status,
    --     credit_score,
    --     primary_bank,
    --     primary_branch
    -- FROM
    --     dedup_customer
    -- WHERE
    --     customer_rank = 1
    --     AND customer_code='CUS10007'
)

SELECT
    customer_code,
    first_name,
    last_name,
    id_number,
    date_of_birth,
    gender,
    email,
    phone_number,
    province,
    city,
    postal_code,
    income_bracket,
    employment_status,
    credit_score,
    primary_bank,
    primary_branch,
    MD5(CONCAT(first_name, last_name, id_number, date_of_birth, gender, email, phone_number, province, city, postal_code, income_bracket, employment_status, credit_score, primary_bank, primary_branch)) AS change_hash
FROM stg_customers