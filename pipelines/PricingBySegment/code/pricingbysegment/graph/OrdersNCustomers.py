from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *

def OrdersNCustomers(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").save("dbfs:/Prophecy/sparklearner123@gmail.com/Pricing/OrdersNCustomers")
