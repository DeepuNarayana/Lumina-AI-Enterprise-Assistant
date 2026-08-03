from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str ="Lumina AI"

    DATABASE_URL: str

    SECRET_KEY : str

    AWS_REGION : str

    S3_BUCKET_NAME : str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

@lru_cache
def get_settings()->Settings:
    return Settings()

settings=get_settings()