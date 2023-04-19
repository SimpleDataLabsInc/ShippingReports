from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from retail.config.ConfigStore import *
from retail.udfs.UDFs import *

def FullName(spark: SparkSession, TotalByCustomer: DataFrame) -> DataFrame:
    return TotalByCustomer.select(
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        round(col("amounts")).alias("amounts"), 
        concat(col("first_name"), lit(" "), col("last_name")).alias("full_name")
    )
