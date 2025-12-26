# 🧾 Spark-Based Big Data Processing on GCP (Dataproc + BigQuery)

## 📌 Project Overview

This project demonstrates **large-scale data processing** using **Apache Spark on Google Cloud Dataproc**.  
Retail data is ingested from **Google Cloud Storage (GCS)**, processed using **PySpark**, and loaded into  
**Google BigQuery** for analytics.

The project is designed to reflect **real-world Data Engineering practices** on GCP.

## 🧰 Technologies Used

- **Apache Spark (PySpark)**
- **Google Cloud Dataproc**
- **Google Cloud Storage (GCS)**
- **Google BigQuery**
- **Python**
- **YAML (Configuration-driven design)**

---

## 📁 Project Structure

The directory layout of the \texttt{spark-online-retail} project is shown below:

```
spark-online-retail/
│
├── spark_jobs/
│   ├── main.py
│   ├── orders_processing.py
│   ├── customers_processing.py
│   └── country_sales_processing.py
│
├── config/
│   └── config.yaml
│
├── dataproc/
│   └── submit_job.sh
│
└── README.md
```

---

## 📂 Input Data (GCS)

Raw retail data is stored in Google Cloud Storage:
gs://superstore-retail-code/raw-data/


Spark reads **all CSV files** present in this directory, enabling scalable and distributed ingestion.

---

## 🔄 Data Processing Flow
### 1️⃣ Orders Processing

Reads orders data from GCS

Parses dates and casts numeric fields

Writes cleaned data to BigQuery orders table

### 2️⃣ Customers Processing

Extracts customer-related attributes

Removes duplicate records

Writes data to BigQuery customers table

### 3️⃣ Country-Level Sales Aggregation

Groups data by country

Computes total sales, profit, and quantity

Writes aggregated results to BigQuery country_sales table

## 🚀 Running the Spark Job on Dataproc

Submit the Spark job using Cloud Shell or any environment with gcloud installed.

## 🪣 BigQuery Temporary GCS Bucket

The Spark–BigQuery connector requires a temporary GCS bucket for staging data.

superstore-bq-temp


This bucket is used internally during Spark → BigQuery writes and is automatically cleaned up.

## 📊 BigQuery Output Tables

| **Table Name**   | **Description**                          |
|------------------|------------------------------------------|
| `orders`         | Cleaned order-level data                 |
| `customers`      | Customer master data                     |
| `country_sales`  | Aggregated country-level sales data      |

---

## 🔑 Key Spark Concepts Demonstrated

- **Transformations vs Actions**
- **Lazy Evaluation**
- **Distributed file reads from GCS**
- **Aggregations and GroupBy operations**
- **Spark–BigQuery Connector usage**
- **Cloud-native Spark execution on Dataproc**
