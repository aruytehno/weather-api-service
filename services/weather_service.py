from db.database import db
from models.weather import WeatherCreate
from bson import ObjectId


async def save_weather(data: WeatherCreate) -> str:
    result = await db.weather_cache.insert_one(data.dict())
    return str(result.inserted_id)


async def get_latest_weather(city: str):
    result = await db.weather_cache.find_one({"city": city}, sort=[("timestamp", -1)])
    if result:
        result["id"] = str(result["_id"])
        return result
    return None
