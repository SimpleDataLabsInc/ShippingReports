from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def PricingReport_1(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder
    in0.write\
        .format("delta")\
        .option("mergeSchema", True)\
        .mode("overwrite")\
        .save("dbfs:/Prophecy/sparklearner123@gmail.com/Shipping/Report")
