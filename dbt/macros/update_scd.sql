{% macro update_scd(table_name, load_date) %}

    UPDATE {{ table_name }}
        SET end_date = CAST('{{ load_date }}' AS DATE),
            current_flag = FALSE
        WHERE customer_code IN (
            SELECT t.customer_code
            FROM {{ table_name }} t
            JOIN {{ ref('stg_customers') }} s
                ON t.customer_code = s.customer_code
            WHERE t.change_hash <> s.change_hash
                AND t.current_flag = TRUE
        )
        AND current_flag = TRUE
        AND start_date < CAST('{{ load_date }}' AS DATE)

{% endmacro %}