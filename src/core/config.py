from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    VERSION = "0.0.1"
    RELEASE_ID = "0.0.1"

    class Config:
        case_sensitive = True


settings = Settings()
