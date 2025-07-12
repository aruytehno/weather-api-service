from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "weather_app"

    class Config:
        env_file = ".env"


settings = Settings()

class Settings(BaseSettings):
    ...
    OPENWEATHER_API_KEY: str
    ...
