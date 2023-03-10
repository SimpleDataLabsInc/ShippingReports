from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(
            self,
            env: str=None, 
            another_variable: bool=None, 
            yet_another_variable: float=None, 
            encrypt_logic: str=None
    ):
        self.spark = None
        self.update(env, another_variable, yet_another_variable, encrypt_logic)

    def update(
            self,
            env: str="dev", 
            another_variable: bool=True, 
            yet_another_variable: float=2.0, 
            encrypt_logic: str="aes_encrypt(COMMENT, secret('dev-scope', 'AESkey'))"
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.env = env
        self.another_variable = self.get_bool_value(another_variable)
        self.yet_another_variable = self.get_float_value(yet_another_variable)
        self.encrypt_logic = encrypt_logic
        pass
