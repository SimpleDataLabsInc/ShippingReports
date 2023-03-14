from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def BySegment(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        ((col("FOLLOW_UP") == expr(Config.follow_up_logic)) & (col("MKTSEGMENT") == lit(Config.market_segment)))
    )
