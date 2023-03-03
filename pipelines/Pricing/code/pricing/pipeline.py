from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricing.config.ConfigStore import *
from pricing.udfs.UDFs import *
from prophecy.utils import *
from pricing.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Customer = Customer(spark)
    df_Orders = Orders(spark)
    df_Shipments = Shipments(spark)
    df_Reformat = Reformat(spark, df_Shipments)
    df_Join = Join(spark, df_Reformat, df_Orders, df_Customer)
    df_Where = Where(spark, df_Join)
    df_SumRevenue = SumRevenue(spark, df_Where)
    df_Date = Date(spark, df_SumRevenue)
    df_ColNames = ColNames(spark, df_Date)
    df_Cleanup = Cleanup(spark, df_Reformat)
    df_SumAmounts = SumAmounts(spark, df_Cleanup)
    df_ByStatus = ByStatus(spark, df_SumAmounts)
    ReportPrices(spark, df_ByStatus)
    Unshipped(spark, df_ColNames)

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
