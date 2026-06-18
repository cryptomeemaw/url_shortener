from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    ENV: str
    DATABASE_URL: str
    BASE_URL: str
    CODE_LENGTH: int

app_config = AppConfig()

