from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *
from prophecy.utils import *
from pricingbysegment.graph import *

def pipeline(spark: SparkSession) -> None:
    df_OrdersNCustomers_1 = OrdersNCustomers_1(spark)
    df_Shipments = Shipments(spark)
    df_ByOrderkey = ByOrderkey(spark, df_Shipments, df_OrdersNCustomers_1)
    df_ByOrderkey = df_ByOrderkey.cache()
    df_AdjustCols = AdjustCols(spark, df_ByOrderkey)
    df_BySegment = BySegment(spark, df_AdjustCols)
    df_SumAmounts = SumAmounts(spark, df_BySegment)
    PricingReport(spark, df_SumAmounts)
    df_Shipments_old = Shipments_old(spark)
    df_Customer_TPCH = Customer_TPCH(spark)
    df_Cleanup = Cleanup(spark, df_Shipments_old)
    df_SumAmounts_old = SumAmounts_old(spark, df_Cleanup)
    df_ByStatus = ByStatus(spark, df_SumAmounts_old)
    PricingReport_old(spark, df_ByStatus)
    df_Orders_TPCH = Orders_TPCH(spark)
    df_Join_1 = Join_1(spark, df_Customer_TPCH, df_Orders_TPCH)
    OrdersNCustomers(spark, df_Join_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PricingBySegment")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PricingBySegment")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
