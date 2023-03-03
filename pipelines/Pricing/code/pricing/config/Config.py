from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, segment: str=None, path_helper: str=None):
        self.spark = None
        self.update(segment, path_helper)

    def update(self, segment: str="AUTOMOBILE", path_helper: str="Path0"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.segment = segment
        self.path_helper = path_helper
        pass
