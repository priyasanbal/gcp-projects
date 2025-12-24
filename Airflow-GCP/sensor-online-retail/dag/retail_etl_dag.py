from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor



from transformation.clean_retail_data import clean_online_retail
from loading.load_to_bigquery import load_online_retail_to_bq

default_args = {
    "owner": "data-engineer",
    "retries": 1
}

with DAG(
    dag_id="sensor-online-reatil",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    # 1️⃣ FILE WATCHER (SENSOR)
    wait_for_retail_file = GCSObjectExistenceSensor(
        task_id="wait_for_online_retail_file",
        bucket="sensor-onlinestore-rawdata",
        object="sensor-retail/sensor-ingestion-23-12-2025/sensor_online_retail.csv",
        poke_interval=60,        # check every 60 seconds
        timeout=60 * 60,         # wait max 1 hour
        mode="poke"
    )

    transform = PythonOperator(
        task_id="clean_retail_data",
        python_callable=clean_online_retail
    )

    load = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_online_retail_to_bq
    )

    wait_for_retail_file  >> transform >> load
