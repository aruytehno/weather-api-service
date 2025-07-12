import httpx
from db.config import settings


async def fetch_weather_from_api(city: str):
    api_key = settings.OPENWEATHER_API_KEY
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={api_key}&units=metric&lang=ru"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
