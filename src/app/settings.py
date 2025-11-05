from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    JWT_SECRET: str = "change_me_now"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
