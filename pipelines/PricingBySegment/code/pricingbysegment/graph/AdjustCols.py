from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def AdjustCols(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("MKTSEGMENT"), 
        col("QUANTITY"), 
        col("EXTENDEDPRICE"), 
        col("DISCOUNT"), 
        col("TAX"), 
        col("RETURNFLAG"), 
        col("DELIVERYSTATUS"), 
        when(((col("DISCOUNT") > lit(0.06)) | col("RETURNFLAG").eqNullSafe(lit(True))), lit("true"))\
          .otherwise(lit("false"))\
          .alias("CLEARANCE"), 
        col("ORDERKEY"), 
        col("CUSTKEY")
    )
