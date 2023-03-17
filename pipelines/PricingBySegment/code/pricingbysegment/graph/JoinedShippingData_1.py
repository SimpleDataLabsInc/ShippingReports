from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def JoinedShippingData_1(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Prophecy/sparklearner123@gmail.com/Receiving/JoinedShippingData")
