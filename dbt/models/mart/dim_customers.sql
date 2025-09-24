{{ config(
    materialized='incremental',
    incremental_strategy='append',
    unique_key='customer_code',
    on_schema_change='sync_all_columns'
) }}

select
    *
from {{ ref('hist_customers') }}