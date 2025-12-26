from pyspark.sql import SparkSession
import yaml

from orders_processing import process_orders
from customers_processing import process_customers
from country_sales import process_country_sales

spark = SparkSession.builder \
    .appName("OnlineRetailSparkPipeline") \
    .getOrCreate()

with open("config.yaml") as f:
    config = yaml.safe_load(f)

orders_df = process_orders(spark, config)
customers_df = process_customers(spark, config)
process_country_sales(orders_df, config)

spark.stop()
