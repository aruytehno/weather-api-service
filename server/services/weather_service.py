from server.db import db
from server.models import WeatherCreate
from typing import List

async def save_weather(data: WeatherCreate) -> str:
    result = await db.weather_cache.insert_one(data.dict())
    return str(result.inserted_id)


async def get_latest_weather(city: str):
    result = await db.weather_cache.find_one({"city": city}, sort=[("timestamp", -1)])
    if result:
        result["id"] = str(result["_id"])
        return result
    return None


async def get_weather_history(city: str, limit: int = 10) -> List[dict]:
    cursor = db.weather_cache.find({"city": city}).sort("timestamp", -1).limit(limit)
    history = []
    async for document in cursor:
        document["id"] = str(document["_id"])
        history.append(document)
    return history
