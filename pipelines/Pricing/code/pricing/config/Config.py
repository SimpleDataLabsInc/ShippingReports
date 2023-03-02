from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, segment: str=None, datestring: str=None, Database: str=None, path_helper: str=None):
        self.spark = None
        self.update(segment, datestring, Database, path_helper)

    def update(
            self,
            segment: str="BUILDING", 
            datestring: str="1993-11-13", 
            Database: str="RETAIL", 
            path_helper: str="Path1"
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.segment = segment
        self.datestring = datestring
        self.Database = Database
        self.path_helper = path_helper
        pass
