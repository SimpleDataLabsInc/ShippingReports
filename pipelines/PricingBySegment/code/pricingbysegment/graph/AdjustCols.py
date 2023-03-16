from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def AdjustCols(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("C_MKTSEGMENT").alias("MKTSEGMENT"), 
        expr(Config.follow_up_criteria).alias("FOLLOW_UP"), 
        col("QUANTITY"), 
        col("EXTENDEDPRICE"), 
        col("DISCOUNT"), 
        col("TAX"), 
        col("RETURNFLAG"), 
        col("DELIVERYSTATUS"), 
        when(((col("DISCOUNT") > lit(0.06)) | col("RETURNFLAG").eqNullSafe(lit(True))), lit("true"))\
          .otherwise(lit("false"))\
          .alias("CLEARANCE"), 
        col("SHIPDATE"), 
        col("C_ACCTBAL").alias("ACCTBAL"), 
        col("C_CUSTKEY"), 
        col("ORDERKEY")
    )
