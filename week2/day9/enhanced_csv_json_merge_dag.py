from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import json
import psycopg2

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

dag = DAG(
    "enhanced_csv_json_merge_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="ETL merging CSV and JSON, normalizing and inserting to PostgreSQL"
)

def load_and_merge_data(**kwargs):
    df_csv = pd.read_csv("/opt/airflow/dags/employees_info.csv")
    with open("/opt/airflow/dags/performance_data.json", "r") as f:
        data_json = json.load(f)
    df_json = pd.DataFrame(data_json["performance"])
    df = pd.merge(df_csv, df_json, on="id")
    df["seniority"] = df["tenure_years"].apply(lambda x: "Senior" if x >= 3 else "Junior")
    df.to_csv("/opt/airflow/dags/enriched_employees.csv", index=False)
    print("Merged and enriched CSV written")

def insert_into_postgres(**kwargs):
    df = pd.read_csv("/opt/airflow/dags/enriched_employees.csv")
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )
    cur = conn.cursor()

    # Normalize: insert departments and countries
    for _, row in df.iterrows():
        cur.execute("INSERT INTO department (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (row["department"],))
        cur.execute("SELECT department_id FROM department WHERE name = %s", (row["department"],))
        dept_id = cur.fetchone()[0]

        cur.execute("INSERT INTO country (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (row["country"],))
        cur.execute("SELECT country_id FROM country WHERE name = %s", (row["country"],))
        country_id = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO employee (id, name, age, salary, department_id, country_id) "
            "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
            (row["id"], row["name"], row["age"], row["salary"], dept_id, country_id)
        )

        # Insert performance score
        cur.execute(
            "INSERT INTO performance (employee_id, review_score, tenure_years, seniority) "
            "VALUES (%s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING",
            (row["id"], row["review_score"], row["tenure_years"], row["seniority"])
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted into PostgreSQL")

load_task = PythonOperator(
    task_id="load_and_merge",
    python_callable=load_and_merge_data,
    dag=dag
)

insert_task = PythonOperator(
    task_id="insert_postgres",
    python_callable=insert_into_postgres,
    dag=dag
)

load_task >> insert_task
