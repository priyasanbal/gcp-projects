from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


from transformation.clean_retail_data import clean_online_retail
from loading.load_to_bigquery import load_online_retail_to_bq

default_args = {
    "owner": "data-engineer",
    "retries": 1
}

with DAG(
    dag_id="online_retail_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    

    transform = PythonOperator(
        task_id="clean_sales_data",
        python_callable=clean_online_retail
    )

    load = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_online_retail_to_bq
    )

    transform >> load
