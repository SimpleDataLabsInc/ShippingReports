from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, encrypt_logic: str=None, tax_logic: str=None):
        self.spark = None
        self.update(encrypt_logic, tax_logic)

    def update(
            self,
            encrypt_logic: str="aes_encrypt(COMMENT, '1234567890123456')", 
            tax_logic: str="cast(if(TAX == 0, 0.02, TAX) as decimal(12,2))"
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.encrypt_logic = encrypt_logic
        self.tax_logic = tax_logic
        pass
