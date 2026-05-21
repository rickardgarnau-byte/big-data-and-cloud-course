from pyspark import pipelines as dp

BASE_DIR = "/Volumes/airbnb/hosts/csv_files"

schema = (
    spark.read.format("csv")
    .options(header=True, inferSchema=True)
    .load(f"{BASE_DIR}/Airbnb_Open_Data.csv")
    .schema
)


@dp.table(
    name="raw_supply_chain",
    comment="Raw data from Airbnb",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5",
    })

def raw_supply_chain():
    return (
        spark.readStream.format("csv")
        .option("header", "True")
        .option("encoding", "utf-8")
        .schema(schema)
        .load(f"{BASE_DIR}/")
    )
    
