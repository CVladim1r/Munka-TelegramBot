from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    DB_CONFIG: dict
    model_config: SettingsConfigDict = SettingsConfigDict (
        env_file=".env",
        env_file_encoding="utf-8"
    )