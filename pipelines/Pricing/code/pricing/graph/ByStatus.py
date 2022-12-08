from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def ByStatus(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("RETURNFLAG").asc(), col("DELIVERYSTATUS").asc())
