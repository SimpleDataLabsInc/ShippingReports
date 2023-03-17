from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, wholesale_discount: float=None):
        self.spark = None
        self.update(market_segment, wholesale_discount)

    def update(self, market_segment: str="AUTOMOBILE", wholesale_discount: float=0.05):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.market_segment = market_segment
        self.wholesale_discount = self.get_float_value(wholesale_discount)
        pass
