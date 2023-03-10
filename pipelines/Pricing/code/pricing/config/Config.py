from prophecy.config import ConfigBase
prophecy_spark_context = None


class Config(ConfigBase):

    def __init__(self, env: str=None, encryption_logic: str=None):
        self.spark = None
        self.update(env, encryption_logic)

    def update(self, env: str="dev", encryption_logic: str="aes_encrypt(COMMENT, secret('dev-scope', 'AESkey'))"):
        global prophecy_spark_context
        prophecy_spark_context = self.spark
        self.env = env
        self.encryption_logic = encryption_logic
        pass
