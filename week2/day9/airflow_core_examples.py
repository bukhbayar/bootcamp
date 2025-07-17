# --- DAG Structure in Code ---
from airflow import DAG
from datetime import datetime

# Define a basic DAG
with DAG(
    dag_id="example_dag_structure",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    pass  # Tasks will be defined here


# --- PythonOperator Example ---
from airflow.operators.python import PythonOperator

def greet():
    print("Hello from Airflow!")

greet_task = PythonOperator(
    task_id="greet_task",
    python_callable=greet
)


# --- Task Dependencies ---
from airflow.operators.dummy import DummyOperator

start = DummyOperator(task_id="start")
process = DummyOperator(task_id="process")
end = DummyOperator(task_id="end")

start >> process >> end  # Set task order


# --- Scheduling DAGs ---
from airflow import DAG
from datetime import datetime

# DAG scheduled at 6am daily
with DAG(
    dag_id="scheduled_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="0 6 * * *",
    catchup=False
) as dag:
    pass


# --- Monitoring DAGs ---
from airflow.operators.python import PythonOperator

def log_example(**kwargs):
    print("Task instance info:", kwargs['ti'])

log_task = PythonOperator(
    task_id="log_task",
    python_callable=log_example
)


# --- Retrying Failed Tasks ---
from airflow.operators.python import PythonOperator
from datetime import timedelta
import random

def might_fail():
    if random.random() < 0.5:
        raise Exception("Simulated failure")
    print("Succeeded!")

retry_task = PythonOperator(
    task_id="retry_task",
    python_callable=might_fail,
    retries=3,
    retry_delay=timedelta(minutes=5)
)
