from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):

    APP_NAME: str = "FMB System Anti-Fraud"

    VERSION: str = "1.0.0"

    DEBUG: bool = False

    DATABASE_URL: str = "sqlite:///./data/fraud_master_bank.db"

    REDIS_URL: str = "redis://localhost:6379"

    EVENT_STORE_TABLE: str = "events"

    FEATURE_STORE_TABLE: str = "features"

    GRAPH_DB_URL: str = "bolt://localhost:7687"

    API_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("DEBUG", mode="before")
    @classmethod
    def _parse_debug(cls, value):
        if isinstance(value, str):
            lowered = value.strip().lower()
            if lowered in {"release", "prod", "production"}:
                return False
        return value


settings = Settings()
