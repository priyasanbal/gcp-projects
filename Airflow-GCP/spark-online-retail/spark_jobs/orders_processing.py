from pyspark.sql.functions import col, to_date

def process_orders(spark, config):
    orders_df = spark.read.option("header", True).csv(
        config["gcs"]["raw_data"]
    )

    orders_df = orders_df.select(
        "Row ID", "Order ID", "Order Date", "Ship Date",
        "Ship Mode", "Product ID", "Category",
        "Sub-Category", "Product Name",
        "Sales", "Quantity", "Discount", "Profit", "Country"
    )

    # Write Orders to GCS
    orders_df.write.mode("overwrite") \
        .parquet(config["gcs"]["processed_orders"])

    # Write Orders to BigQuery
    orders_df.write.format("bigquery") \
        .option("table", config["bigquery"]["orders_table"]) \
        .option("temporaryGcsBucket", "superstore-bq-temp") \
        .mode("overwrite") \
        .save()

    return orders_df
