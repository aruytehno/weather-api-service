from pydantic_settings import BaseSettings
from pathlib import Path

# Путь к .env (на 2 уровня выше config.py)
env_path = Path(__file__).parent.parent.parent / ".env"

class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "weather_app"
    OPENWEATHER_API_KEY: str

    class Config:
        env_file = env_path
        env_file_encoding = "utf-8"

settings = Settings()
print("🔄 Загруженные настройки:")
print(f"MONGO_URL = {settings.MONGO_URL}")
print(f"DB_NAME = {settings.DB_NAME}")
print(f"OPENWEATHER_API_KEY = {settings.OPENWEATHER_API_KEY}")