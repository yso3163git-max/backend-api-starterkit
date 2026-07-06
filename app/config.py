from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  app_name: str = "Backend API Starter Kit"
  app_version: str = "0.1.0"
  debug: bool = False
  api_prefix: str = "/api/v1"
  host: str = "0.0.0.0"
  port: int = 8000
  cors_origins: list[str] = ["http://localhost:3000"]

  class Config:
    env_file = ".env"


@lru_cache
def get_settings() -> Settings:
  return Settings()
