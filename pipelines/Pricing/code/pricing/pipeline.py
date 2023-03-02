from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *
from prophecy.utils import *
from pricing.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Customer_TPCH = Customer_TPCH(spark)
    df_Orders_TPCH = Orders_TPCH(spark)
    df_Shipments = Shipments(spark)
    df_Reformat_1 = Reformat_1(spark, df_Shipments)
    df_Join = Join(spark, df_Reformat_1, df_Orders_TPCH, df_Customer_TPCH)
    df_Where = Where(spark, df_Join)
    df_SumRevenue = SumRevenue(spark, df_Where)
    df_Date = Date(spark, df_SumRevenue)
    UnshippedOrders(spark, df_Date)
    df_Cleanup = Cleanup(spark, df_Reformat_1)
    df_SumAmounts = SumAmounts(spark, df_Cleanup)
    df_ByStatus = ByStatus(spark, df_SumAmounts)
    ReportPrices(spark, df_ByStatus)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pricing")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pricing")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
