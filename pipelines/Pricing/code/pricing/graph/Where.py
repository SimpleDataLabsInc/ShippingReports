from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def Where(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        (
          (((col("C_MKTSEGMENT") == lit(Config.segment)) & (col("C_CUSTKEY") == col("O_CUSTKEY"))) & (col("L_ORDERKEY") == col("O_ORDERKEY")))
          & ((col("O_ORDERDATE") < lit("1995-03-15")) & (col("L_SHIPDATE") < lit("1995-03-15")))
        )
    )
