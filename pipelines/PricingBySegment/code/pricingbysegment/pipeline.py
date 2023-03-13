from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricingbysegment.config.ConfigStore import *
from pricingbysegment.udfs.UDFs import *
from prophecy.utils import *
from pricingbysegment.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Shipments = Shipments(spark)
    df_Cleanup = Cleanup(spark, df_Shipments)
    df_SumAmounts = SumAmounts(spark, df_Cleanup)
    df_ByStatus = ByStatus(spark, df_SumAmounts)
    PricingReport(spark, df_ByStatus)
    df_Source_1 = Source_1(spark)

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
