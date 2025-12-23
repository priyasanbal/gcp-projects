# Sensor-Based Online Retail ETL Pipeline (GCP + Airflow)

## Overview

This project implements a **sensor-driven ETL pipeline** for an **Online Retail dataset** using **Apache Airflow (Cloud Composer)** on **Google Cloud Platform (GCP)**.

The pipeline waits for a CSV file to arrive in **Google Cloud Storage (GCS)** and then automatically:
- Cleans the retail data
- Loads the transformed data into **BigQuery**

This design follows a **file-arrival–based (event-aware) batch processing approach**.

---

## What the Pipeline Does

1. Watches a GCS bucket for the arrival of an online retail CSV file
2. Once the file is detected:
   - Cleans and transforms the data using Python
   - Loads the processed data into BigQuery
3. Orchestrates the entire flow using Airflow

---

## Tech Stack

- Google Cloud Platform (GCP)
- Apache Airflow (Cloud Composer)
- Google Cloud Storage (GCS)
- BigQuery
- Python
- Pandas

---

## Project Structure

```text
dags/
├── sensor_online_retail_dag.py
│
├── transformation/
│   └── clean_retail_data.py
│
├── loading/
│   └── load_to_bigquery.py
│
├── config/
│   └── config.yaml
│
└── README.md
