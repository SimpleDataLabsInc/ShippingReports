from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def SumRevenue(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(
        col("C_MKTSEGMENT"), 
        col("L_ORDERKEY"), 
        col("O_ORDERDATE"), 
        col("`O_SHIP-PRIORITY`").alias("O_SHIP-PRIORITY")
    )

    return df1.agg(
        sum((col("L_EXTENDEDPRICE") * (lit(1) - col("L_DISCOUNT")))).cast(DecimalType(34, 2)).alias("REVENUE")
    )
