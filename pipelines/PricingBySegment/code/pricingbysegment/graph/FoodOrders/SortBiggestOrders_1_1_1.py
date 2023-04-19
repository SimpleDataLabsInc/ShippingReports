from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pricingbysegment.udfs.UDFs import *

def SortBiggestOrders_1_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("amounts").desc())
