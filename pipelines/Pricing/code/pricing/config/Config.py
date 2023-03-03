from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, segment: str=None, my_expression: str=None):
        self.spark = None
        self.update(segment, my_expression)

    def update(self, segment: str="MACHINERY", my_expression: str="!equal_null(C_CUSTKEY, O_ORDERKEY)"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.segment = segment
        self.my_expression = my_expression
        pass
