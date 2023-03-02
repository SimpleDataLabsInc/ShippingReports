from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, segment: str=None, datestring: str=None, Database: str=None):
        self.spark = None
        self.update(segment, datestring, Database)

    def update(self, segment: str="BUILDING", datestring: str="1993-11-13", Database: str="RETAIL"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.segment = segment
        self.datestring = datestring
        self.Database = Database
        pass
