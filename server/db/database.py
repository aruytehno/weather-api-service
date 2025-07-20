from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings  # импорт объекта настроек из config.py

client = AsyncIOMotorClient(settings.MONGO_URL)
db = client[settings.DB_NAME]
