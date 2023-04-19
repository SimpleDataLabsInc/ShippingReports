from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, env: str=None, another_var: bool=None, encrypt_logic: str=None, **kwargs):
        self.spark = None
        self.update(env, another_var, encrypt_logic)

    def update(
            self,
            env: str="dev",
            another_var: bool=False,
            encrypt_logic: str="aes_encrypt(COMMENT, secret('dev-scope', 'AESkey'))",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.env = env
        self.another_var = self.get_bool_value(another_var)
        self.encrypt_logic = encrypt_logic
        pass
