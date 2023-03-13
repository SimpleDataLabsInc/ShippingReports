from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def SumAmounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("RETURNFLAG"), col("DELIVERYSTATUS"))

    return df1.agg(
        sum(col("QUANTITY")).alias("SUM_QTY"), 
        format_number(avg(col("QUANTITY")), 2).alias("AVG_QTY"), 
        format_number(sum(((col("EXTENDEDPRICE") * (lit(1) - col("DISCOUNT"))) * (lit(1) + col("TAX")))), 2)\
          .alias("SUM_CHARGE"), 
        count(lit(1)).alias("COUNT_ORDER"), 
        expr("count_if((CLEARANCE = 'true'))").alias("COUNT_CLEARANCE")
    )
