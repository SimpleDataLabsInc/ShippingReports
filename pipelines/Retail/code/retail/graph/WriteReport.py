from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from retail.config.ConfigStore import *
from retail.udfs.UDFs import *

def WriteReport(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").save("dbfs:/Prophecy/sparklearner123@gmail.com/CustomersOrdersReport")
