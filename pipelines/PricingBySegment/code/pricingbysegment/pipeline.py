from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *
from prophecy.utils import *
from pricingbysegment.graph import *

def pipeline(spark: SparkSession) -> None:
    df_JoinedShippingData = JoinedShippingData(spark)
    df_Columns = Columns(spark, df_JoinedShippingData)
    df_Columns = df_Columns.cache()
    df_OrdersNCustomers_1 = OrdersNCustomers_1(spark)
    df_BySegment = BySegment(spark, df_Columns)
    df_BySegment = df_BySegment.cache()
    df_Amounts = Amounts(spark, df_BySegment)
    df_AdjustCols_V2 = AdjustCols_V2(spark)
    df_AdjustCols_V2 = df_AdjustCols_V2.cache()
    df_ForFollowUp_V2 = ForFollowUp_V2(spark, df_AdjustCols_V2)
    df_ForFollowUp_V2 = df_ForFollowUp_V2.cache()
    df_SumAmounts_V2 = SumAmounts_V2(spark, df_ForFollowUp_V2)
    PricingReport_V2(spark, df_SumAmounts_V2)
    df_Shipments = Shipments(spark)
    df_ByOrderkey = ByOrderkey(spark, df_Shipments, df_OrdersNCustomers_1)
    df_ByOrderkey = df_ByOrderkey.cache()
    df_Shipments_old = Shipments_old(spark)
    df_Customer_TPCH = Customer_TPCH(spark)
    df_Cleanup = Cleanup(spark, df_Shipments_old)
    df_SumAmounts_old = SumAmounts_old(spark, df_Cleanup)
    df_ByStatus = ByStatus(spark, df_SumAmounts_old)
    PricingReport_old(spark, df_ByStatus)
    JoinedShippingData_1(spark, df_ByOrderkey)
    df_Orders_TPCH = Orders_TPCH(spark)
    df_Join_1 = Join_1(spark, df_Customer_TPCH, df_Orders_TPCH)
    OrdersNCustomers(spark, df_Join_1)
    PricingReport_1(spark, df_Amounts)

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
