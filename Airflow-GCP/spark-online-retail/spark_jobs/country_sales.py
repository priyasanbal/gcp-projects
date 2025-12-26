from pyspark.sql import functions as F

def process_country_sales(orders_df, config):
    country_sales_df = (
        orders_df
        .groupBy("Country")
        .agg(
            F.round(F.sum("Sales"), 2).alias("total_sales"),
            F.round(F.sum("Profit"), 2).alias("total_profit"),
            F.sum("Quantity").alias("total_quantity"),
            F.round(F.avg("Discount"), 2).alias("avg_discount"),
            F.countDistinct("Order ID").alias("order_count")
        )
    )

    # Write to GCS
    country_sales_df.write.mode("overwrite") \
        .parquet(config["gcs"]["country_sales_output"])

    # Write to BigQuery
    country_sales_df.write.format("bigquery") \
        .option("table", config["bigquery"]["country_sales_table"]) \
        .option("temporaryGcsBucket", "superstore-bq-temp") \
        .mode("overwrite") \
        .save()
