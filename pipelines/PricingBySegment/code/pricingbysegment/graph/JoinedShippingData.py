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
            StructField("MKTSEGMENT", StringType(), True), StructField("QUANTITY", DecimalType(12, 2), True), StructField("EXTENDEDPRICE", DecimalType(12, 2), True), StructField("DISCOUNT", DecimalType(12, 2), True), StructField("TAX", DecimalType(12, 2), True), StructField("RETURNFLAG", StringType(), True), StructField("DELIVERYSTATUS", StringType(), True), StructField("CUSTKEY", StringType(), True), StructField("ORDERKEY", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/sparklearner123@gmail.com/Receiving/JoinedShippingData")
