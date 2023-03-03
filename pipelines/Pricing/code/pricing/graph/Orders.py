from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Orders(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("O_ORDERKEY", StringType(), True), StructField("O_CUSTKEY", StringType(), True), StructField("O_ORDERSTATUS", StringType(), True), StructField("O_TOTALPRICE", StringType(), True), StructField("O_ORDERDATE", DateType(), True), StructField("O_ORDER-PRIORITY", StringType(), True), StructField("O_CLERK", StringType(), True), StructField("O_SHIP-PRIORITY", StringType(), True), StructField("O_COMMENT", StringType(), True)
        ])
        )\
        .option("header", False)\
        .option("sep", "|")\
        .csv("dbfs:/databricks-datasets/tpch/data-001/orders/orders.tbl")
