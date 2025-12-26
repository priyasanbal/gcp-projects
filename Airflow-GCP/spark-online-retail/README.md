gcs:
  raw_data: gs://online-retail-raw/superstore/
  processed_orders: gs://online-retail-processed/orders/
  processed_customers: gs://online-retail-processed/customers/
  country_sales_output: gs://online-retail-processed/country_sales/

bigquery:
  project: my-project
  dataset: retail_dw
  orders_table: my-project:retail_dw.orders
  customers_table: my-project:retail_dw.customers
  country_sales_table: my-project:retail_dw.country_sales
