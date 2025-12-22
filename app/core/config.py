from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Redis Configuration
    REDIS_NODES: str = ""  # Comma-separated list of redis URLs

    # Consistent Hashing Config
    VIRTUAL_NODES: int = 100

    # Batch Processing Config
    BATCH_INTERVAL_SECONDS: float = 10.0

    # App Config
    DEBUG: bool = True
    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
