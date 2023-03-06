from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("QUANTITY"), 
        col("EXTENDEDPRICE"), 
        col("DISCOUNT"), 
        expr(Config.tax_logic).alias("TAX"), 
        col("RETURNFLAG"), 
        col("DELIVERYSTATUS"), 
        when(((col("DISCOUNT") > lit(0.06)) | col("RETURNFLAG").eqNullSafe(lit(True))), lit("true"))\
          .otherwise(lit("false"))\
          .alias("CLEARANCE")
    )
