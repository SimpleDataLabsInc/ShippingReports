from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from retail.config.ConfigStore import *
from retail.udfs.UDFs import *

def Orders(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("order_id", IntegerType(), True), StructField("customer_id", IntegerType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", DoubleType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .csv("dbfs:/Prophecy/sparklearner123@gmail.com/OrdersDatasetInput.csv")
