from fastapi import APIRouter, HTTPException
from models.weather import WeatherCreate
from services.weather_service import save_weather, get_latest_weather

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
