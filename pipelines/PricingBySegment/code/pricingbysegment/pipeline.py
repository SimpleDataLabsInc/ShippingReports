from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *
from prophecy.utils import *
from pricingbysegment.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Orders = Orders(spark)
    df_Shipments = Shipments(spark)
    df_ByOrderkey = ByOrderkey(spark, df_Shipments, df_Orders)
    df_ByOrderkey = df_ByOrderkey.cache()
    df_AdjustCols = AdjustCols(spark, df_ByOrderkey)
    df_AdjustCols = df_AdjustCols.cache()
    df_BySegment = BySegment(spark, df_AdjustCols)
    df_SumAmounts = SumAmounts(spark, df_BySegment)
    Pricing(spark, df_SumAmounts)

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
