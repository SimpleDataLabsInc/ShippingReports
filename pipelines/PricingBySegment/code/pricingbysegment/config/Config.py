from pricingbysegment.graph.FoodOrders.config.Config import SubgraphConfig as FoodOrders_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, wholesale_discount: float=None, FoodOrders: dict=None, **kwargs):
        self.spark = None
        self.update(market_segment, wholesale_discount, FoodOrders)

    def update(self, market_segment: str="MACHINERY", wholesale_discount: float=0.1, FoodOrders: dict={}, **kwargs):
        prophecy_spark = self.spark
        self.market_segment = market_segment
        self.wholesale_discount = self.get_float_value(wholesale_discount)
        self.FoodOrders = self.get_config_object(
            prophecy_spark, 
            FoodOrders_Config(prophecy_spark = prophecy_spark), 
            FoodOrders, 
            FoodOrders_Config
        )
        pass
