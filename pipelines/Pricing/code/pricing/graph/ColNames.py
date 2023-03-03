from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def ColNames(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("C_MKTSEGMENT").alias("MKTSEGMENT"), 
        col("L_ORDERKEY").alias("ORDERKEY"), 
        col("O_ORDERDATE").alias("ORDERDATE"), 
        col("`O_SHIP-PRIORITY`").alias("SHIP_PRIORITY"), 
        col("REVENUE")
    )
