from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Customer(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("C_CUSTKEY", StringType(), True), StructField("C_NAME", StringType(), True), StructField("C_ADDRESS", StringType(), True), StructField("C_NATIONKEY", StringType(), True), StructField("C_PHONE", StringType(), True), StructField("C_ACCTBAL", StringType(), True), StructField("C_MKTSEGMENT", StringType(), True), StructField("C_COMMENT", StringType(), True)
        ])
        )\
        .option("header", False)\
        .option("sep", "|")\
        .csv("dbfs:/databricks-datasets/tpch/data-001/customer/")
