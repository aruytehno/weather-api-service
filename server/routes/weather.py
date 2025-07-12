from fastapi import APIRouter, HTTPException
from server.services.weather_service import save_weather, get_latest_weather, get_weather_history
from server.utils.openweather import fetch_weather_from_api
from server.models.weather import WeatherCreate
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


@router.get("/history/{city}")
async def get_city_weather_history(city: str, limit: int = 10):
    history = await get_weather_history(city, limit)
    if not history:
        raise HTTPException(status_code=404, detail="No weather data found for city")
    return {"city": city, "history": history}
