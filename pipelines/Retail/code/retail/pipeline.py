from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from retail.config.ConfigStore import *
from retail.udfs.UDFs import *
from prophecy.utils import *
from retail.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Customers = Customers(spark)
    df_Orders = Orders(spark)
    df_PerCustomer = PerCustomer(spark, df_Customers, df_Orders)
    df_TotalByCustomer = TotalByCustomer(spark, df_PerCustomer)
    df_DataCleanup = DataCleanup(spark, Config.DataCleanup, df_TotalByCustomer)
    df_FullName = FullName(spark, df_DataCleanup)
    WriteReport(spark, df_FullName)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Retail")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Retail")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
