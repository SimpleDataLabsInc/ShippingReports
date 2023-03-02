from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *

def UnshippedOrders(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write\
        .format("delta")\
        .mode("overwrite")\
        .save(f"dbfs:/Prophecy/sparklearner123@gmail.com/Pricing/{Config.path_helper}/UnshippedOrders")
