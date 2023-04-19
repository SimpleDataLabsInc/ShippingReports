from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def FoodOrders(spark: SparkSession, config: SubgraphConfig, in0: DataFrame, in1: DataFrame) -> DataFrame:
    Config.update(config)
    df_PerCustomer_1_1_1 = PerCustomer_1_1_1(spark, in0, in1)
    df_TotalByCustomer_1_1_1 = TotalByCustomer_1_1_1(spark, df_PerCustomer_1_1_1)
    df_SortBiggestOrders_1_1_1 = SortBiggestOrders_1_1_1(spark, df_TotalByCustomer_1_1_1)

    return df_SortBiggestOrders_1_1_1
