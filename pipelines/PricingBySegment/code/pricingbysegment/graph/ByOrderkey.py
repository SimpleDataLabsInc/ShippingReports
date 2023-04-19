from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def ByOrderkey(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.ORDERKEY") == col("in1.O_ORDERKEY")), "inner")\
        .select(col("in1.C_MKTSEGMENT").alias("MKTSEGMENT"), col("in0.QUANTITY").alias("QUANTITY"), col("in0.EXTENDEDPRICE").alias("EXTENDEDPRICE"), col("in0.DISCOUNT").alias("DISCOUNT"), col("in0.TAX").alias("TAX"), col("in0.RETURNFLAG").alias("RETURNFLAG"), col("in0.DELIVERYSTATUS").alias("DELIVERYSTATUS"), col("in1.C_CUSTKEY").alias("CUSTKEY"), col("in1.O_ORDERKEY").alias("ORDERKEY"))
