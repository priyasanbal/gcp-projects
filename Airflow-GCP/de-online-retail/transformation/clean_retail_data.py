import yaml
import pandas as pd
from google.cloud import storage
import io

CONFIG_PATH = "/home/airflow/gcs/dags/config/config.yaml"

def clean_online_retail():
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    storage_client = storage.Client()

    # Download raw CSV from GCS
    bucket = storage_client.bucket(config["gcp"]["raw_bucket"])
    blob = bucket.blob(config["paths"]["gcs_raw_online_retail"])
    csv_data = blob.download_as_bytes()

    df = pd.read_csv(io.BytesIO(csv_data))

    # Basic cleaning (realistic rules)
    df.dropna(subset=["CustomerID"], inplace=True)
    df = df[df["Quantity"] > 0]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df.drop_duplicates(inplace=True)

    # Write Parquet to processed bucket
    processed_bucket = storage_client.bucket(config["gcp"]["processed_bucket"])
    parquet_blob = processed_bucket.blob(config["paths"]["gcs_processed_online_retail"])

    parquet_buffer = io.BytesIO()
    df.to_parquet(parquet_buffer, index=False)
    parquet_buffer.seek(0)

    parquet_blob.upload_from_file(parquet_buffer)

    print("✅ Cleaned data written as Parquet to GCS")

if __name__ == "__main__":
    clean_online_retail()
