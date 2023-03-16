from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def JoinedShippingData(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("ORDERKEY", DecimalType(38, 0), True), StructField("PARTKEY", DecimalType(38, 0), True), StructField("SUPPKEY", DecimalType(38, 0), True), StructField("LINENUMBER", DecimalType(38, 0), True), StructField("QUANTITY", DecimalType(12, 2), True), StructField("EXTENDEDPRICE", DecimalType(12, 2), True), StructField("DISCOUNT", DecimalType(12, 2), True), StructField("TAX", DecimalType(12, 2), True), StructField("RETURNFLAG", StringType(), True), StructField("DELIVERYSTATUS", StringType(), True), StructField("SHIPDATE", DateType(), True), StructField("COMMITDATE", DateType(), True), StructField("RECEIPTDATE", DateType(), True), StructField("SHIPINSTRUCT", StringType(), True), StructField("SHIPMODE", StringType(), True), StructField("COMMENT", StringType(), True), StructField("C_CUSTKEY", StringType(), True), StructField("C_NAME", StringType(), True), StructField("C_ADDRESS", StringType(), True), StructField("C_NATIONKEY", StringType(), True), StructField("C_PHONE", StringType(), True), StructField("C_ACCTBAL", DecimalType(20, 10), True), StructField("C_MKTSEGMENT", StringType(), True), StructField("C_COMMENT", StringType(), True), StructField("O_ORDERKEY", StringType(), True), StructField("O_CUSTKEY", StringType(), True), StructField("O_ORDERSTATUS", StringType(), True), StructField("O_TOTALPRICE", StringType(), True), StructField("O_ORDERDATE", DateType(), True), StructField("O_ORDER-PRIORITY", StringType(), True), StructField("O_CLERK", StringType(), True), StructField("O_SHIP-PRIORITY", StringType(), True), StructField("O_COMMENT", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/sparklearner123@gmail.com/Receiving/JoinedShippingData")
