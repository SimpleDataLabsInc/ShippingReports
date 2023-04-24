from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, wholesale_discount: float=None, **kwargs):
        self.spark = None
        self.update(market_segment, wholesale_discount)

    def update(self, market_segment: str="MACHINERY", wholesale_discount: float=0.1, **kwargs):
        prophecy_spark = self.spark
        self.market_segment = market_segment
        self.wholesale_discount = self.get_float_value(wholesale_discount)
        pass
