def process_customers(spark, config):
    customers_df = spark.read.option("header", True).csv(
        config["gcs"]["raw_data"]
    )

    customers_df = customers_df.select(
        "Customer ID", "Customer Name", "Segment",
        "Country", "City", "State", "Postal Code", "Region"
    ).dropDuplicates(["Customer ID"])

    # Write Customers to GCS
    customers_df.write.mode("overwrite") \
        .parquet(config["gcs"]["processed_customers"])

    # Write Customers to BigQuery
    customers_df.write.format("bigquery") \
        .option("table", config["bigquery"]["customers_table"]) \
        .option("temporaryGcsBucket", "superstore-bq-temp") \
        .mode("overwrite") \
        .save()

    return customers_df
