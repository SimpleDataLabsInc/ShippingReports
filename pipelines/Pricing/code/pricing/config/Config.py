from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, env: str=None, another_var: bool=None, encrypt_logic: str=None):
        self.spark = None
        self.update(env, another_var, encrypt_logic)

    def update(
            self,
            env: str="dev", 
            another_var: bool=False, 
            encrypt_logic: str="aes_encrypt(COMMENT, secret('dev-scope', 'AESkey'))"
    ):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.env = env
        self.another_var = self.get_bool_value(another_var)
        self.encrypt_logic = encrypt_logic
        pass
