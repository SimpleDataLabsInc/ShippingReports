from retail.graph.DataCleanup.config.Config import SubgraphConfig as DataCleanup_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, DataCleanup: dict=None, **kwargs):
        self.spark = None
        self.update(DataCleanup)

    def update(self, DataCleanup: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.DataCleanup = self.get_config_object(
            prophecy_spark, 
            DataCleanup_Config(prophecy_spark = prophecy_spark), 
            DataCleanup, 
            DataCleanup_Config
        )
        pass
