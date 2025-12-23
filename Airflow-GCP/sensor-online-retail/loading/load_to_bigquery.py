import yaml
from google.cloud import bigquery

CONFIG_PATH = "/home/airflow/gcs/dags/config/config.yaml"

def load_online_retail_to_bq():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    client = bigquery.Client(project=config["gcp"]["project_id"])

    table_id = f"{config['gcp']['project_id']}." \
               f"{config['gcp']['bq_dataset']}." \
               f"{config['gcp']['bq_table']}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        write_disposition="WRITE_TRUNCATE"
    )

    uri = f"gs://{config['gcp']['processed_bucket']}/" \
          f"{config['paths']['gcs_processed_online_retail']}"

    load_job = client.load_table_from_uri(
        uri,
        table_id,
        job_config=job_config
    )

    load_job.result()
    print("✅ Data loaded into BigQuery")

if __name__ == "__main__":
    load_online_retail_to_bq()
