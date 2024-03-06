from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def my_data_processing_function(**kwargs):
    # <code>
    print("Date processing logic goes here!")


default_args = {
    "owner": "you",
    "start_date": datetime(2024, 3, 6),
    # <add par>
}

dag = DAG(
    "my_data_pipeline",
    default_args=default_args,
    schedule_interval="@daily",  # play's interval
)
