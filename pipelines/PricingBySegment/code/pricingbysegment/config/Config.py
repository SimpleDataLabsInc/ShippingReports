from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, market_segment: str=None, shipdate_interval: int=None, follow_up_logic: str=None):
        self.spark = None
        self.update(market_segment, shipdate_interval, follow_up_logic)

    def update(
            self,
            market_segment: str="'FURNITURE' AND 'BUILDING' AND 'AUTOMOBILE' AND 'MANUFACTURING'", 
            shipdate_interval: int=90, 
            follow_up_logic: str="false"
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.market_segment = market_segment
        self.shipdate_interval = self.get_int_value(shipdate_interval)
        self.follow_up_logic = follow_up_logic
        pass
