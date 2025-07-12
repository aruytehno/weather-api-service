from fastapi import APIRouter, HTTPException
from models.weather import WeatherCreate
from services.weather_service import save_weather, get_latest_weather
from utils.openweather import fetch_weather_from_api
from models.weather import WeatherCreate
from datetime import datetime

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.post("/")
async def save_weather_data(data: WeatherCreate):
    weather_id = await save_weather(data)
    return {"message": "Weather data saved", "id": weather_id}


@router.get("/{city}")
async def get_weather_data(city: str):
    data = await get_latest_weather(city)
    if not data:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return data

@router.get("/fetch/{city}")
async def fetch_weather(city: str):
    weather_data = await fetch_weather_from_api(city)
    if not weather_data:
        raise HTTPException(status_code=404, detail="City not found or API error")

    full_data = WeatherCreate(
        city=weather_data["city"],
        temperature=weather_data["temperature"],
        description=weather_data["description"],
        timestamp=datetime.utcnow(),
    )
    weather_id = await save_weather(full_data)
    return {"message": "Weather fetched and saved", "data": full_data, "id": weather_id}
