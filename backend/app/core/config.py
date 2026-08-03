from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #Database
    DATABASE_URL: str

    #JWT
    SECRET_KEY:str
    ALGORITHM: str ="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int =30

    #aws bedrock
    AWS_REGION: str
    BEDROCK_MODEL_ID: str

    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings=Settings()


