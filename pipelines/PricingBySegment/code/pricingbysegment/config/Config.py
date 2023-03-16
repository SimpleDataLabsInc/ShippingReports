from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, follow_up_criteria: str=None, threshold: float=None):
        self.spark = None
        self.update(market_segment, follow_up_criteria, threshold)

    def update(self, market_segment: str="AUTOMOBILE", follow_up_criteria: str="true", threshold: float=10.0):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.market_segment = market_segment
        self.follow_up_criteria = follow_up_criteria
        self.threshold = self.get_float_value(threshold)
        pass
