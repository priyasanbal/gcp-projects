gcloud dataproc jobs submit pyspark \
  --superstore-retail-cluster \
  --region=us-central1 \
  --files=config/config.yaml \
  spark_jobs/main.py


gcloud dataproc jobs submit pyspark \
  gs://superstore-retail-code/spark_jobs/main.py \
  --py-files=gs://superstore-retail-code/spark_jobs/orders_processing.py,gs://superstore-retail-code/spark_jobs/customers_processing.py,gs://superstore-retail-code/spark_jobs/country_sales.py \
  --files=gs://superstore-retail-code/config/config.yaml \
  --cluster=superstore-retail-cluster \
  --region=us-central1