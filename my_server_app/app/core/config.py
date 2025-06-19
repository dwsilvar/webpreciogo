# my_server_app/app/core/config.py
# app/core/config.py
# Application configuration settings loaded from environment variables.

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    PROJECT_NAME: str = "MyServerApp"
    API_V1_STR: str = "/api/v1"

    # Database settings
    DATABASE_URL: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # Celery settings
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Secret key for security
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()