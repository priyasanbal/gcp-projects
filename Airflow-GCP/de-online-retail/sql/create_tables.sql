CREATE SCHEMA IF NOT EXISTS `de-etl-project.sales_dw`;

CREATE OR REPLACE TABLE `de-etl-project.sales_dw.sales_fact` (
  InvoiceNo STRING,
  StockCode STRING,
  Description STRING,
  Quantity INT64,
  InvoiceDate TIMESTAMP,
  UnitPrice FLOAT64,
  CustomerID STRING,
  Country STRING
)
PARTITION BY DATE(InvoiceDate);
