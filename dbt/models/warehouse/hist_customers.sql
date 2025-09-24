{{ config(
    materialized='incremental',
    incremental_strategy='append',
    unique_key='customer_code',
    post_hook="{{ update_scd(this, var('load_date')) }}"
) }}

WITH stg_customers AS (
    SELECT
        customer_code,
        first_name,
        last_name,
        CONCAT(first_name, ' ', last_name) AS full_name,
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
        change_hash,
        TRUE AS current_flag,
        CAST('{{ var("load_date") }}' AS DATE) AS start_date,
        CAST(NULL AS DATE) as end_date
    FROM
        {{ ref('stg_customers') }} c
)

SELECT
    c.customer_code,
    c.first_name,
    c.last_name,
    c.full_name,
    c.id_number,
    c.date_of_birth,
    c.gender,
    c.email,
    c.phone_number,
    c.province,
    c.city,
    c.postal_code,
    c.income_bracket,
    c.employment_status,
    c.credit_score,
    c.primary_bank,
    c.primary_branch,
    c.change_hash,
    c.current_flag,
    c.start_date,
    c.end_date
FROM stg_customers c

{% if is_incremental() %}

    LEFT JOIN {{ this }} t
        ON c.customer_code = t.customer_code
        AND t.current_flag = TRUE
    WHERE
        (t.change_hash IS NULL OR c.change_hash != t.change_hash)

{% endif %}
