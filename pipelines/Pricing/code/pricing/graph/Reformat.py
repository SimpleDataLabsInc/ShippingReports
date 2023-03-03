from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Reformat(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("ORDERKEY").alias("L_ORDERKEY"), 
        col("PARTKEY").alias("L_PARTKEY"), 
        col("SUPPKEY").alias("L_SUPPKEY"), 
        col("LINENUMBER").alias("L_LINENUMBER"), 
        col("QUANTITY").alias("L_QUANTITY"), 
        col("EXTENDEDPRICE").alias("L_EXTENDEDPRICE"), 
        col("DISCOUNT").alias("L_DISCOUNT"), 
        col("TAX").alias("L_TAX"), 
        col("RETURNFLAG").alias("L_RETURNFLAG"), 
        col("DELIVERYSTATUS").alias("L_DELIVERYSTATUS"), 
        col("SHIPDATE").alias("L_SHIPDATE"), 
        col("COMMITDATE").alias("L_COMMITDATE"), 
        col("RECEIPTDATE").alias("L_RECEIPTDATE"), 
        col("SHIPINSTRUCT").alias("L_SHIPINSTRUCT"), 
        col("SHIPMODE").alias("L_SHIPMODE"), 
        col("COMMENT").alias("L_COMMENT")
    )
