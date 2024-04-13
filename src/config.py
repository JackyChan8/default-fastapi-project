import os
from pydantic_settings import BaseSettings
from pydantic import SecretStr


class AppSettings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    APP_SUMMARY: str
    APP_DESCRIPTION: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASS: SecretStr
    POSTGRES_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: SecretStr

    # Testing
    POSTGRES_HOST_TEST: str
    POSTGRES_PORT_TEST: int
    POSTGRES_USER_TEST: str
    POSTGRES_PASS_TEST: SecretStr
    POSTGRES_NAME_TEST: str

    @staticmethod
    def build_postgres_url(user_db: str, pass_db: str, host_db: str,
                           port_db: int, db_name: str, protocol_db: str = 'postgresql+asyncpg') -> str:
        return f"{protocol_db}://{user_db}:{pass_db}@{host_db}:{port_db}/{db_name}"

    def get_postgres_url(self, is_prod: bool = True) -> str:
        """Get URL Postgres Database"""
        if is_prod:
            return self.build_postgres_url(user_db=self.POSTGRES_USER,
                                           pass_db=self.POSTGRES_PASS.get_secret_value(),
                                           host_db=self.POSTGRES_HOST,
                                           port_db=self.POSTGRES_PORT,
                                           db_name=self.POSTGRES_NAME)
        else:
            return self.build_postgres_url(user_db=self.POSTGRES_USER_TEST,
                                           pass_db=self.POSTGRES_PASS_TEST.get_secret_value(),
                                           host_db=self.POSTGRES_HOST_TEST,
                                           port_db=self.POSTGRES_PORT_TEST,
                                           db_name=self.POSTGRES_NAME_TEST)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = AppSettings()
