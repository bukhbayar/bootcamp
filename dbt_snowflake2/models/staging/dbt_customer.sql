{{ config(
    database='SNOWFLAKE_DEMO',
    schema='staging',
    materialized='table'
) }}

SELECT
    *
FROM
    {{ source('snowflake', 'customer') }} c
    LIMIT 100
