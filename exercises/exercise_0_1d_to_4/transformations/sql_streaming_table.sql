CREATE OR REFRESH STREAMING TABLE raw_supply_chain_sql
COMMENT "Raw data from Airbnb with column mapping enabled"
TBLPROPERTIES (
  "delta.columnMapping.mode" = "name",
  "delta.minReaderVersion" = "2",
  "delta.minWriterVersion" = "5"
)
AS SELECT * FROM STREAM read_files(
  "/Volumes/airbnb/hosts/csv_files/",
  format => "csv",
  header => "true",
  inferSchema => "true"
)