from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class WeatherCreate(BaseModel):
    city: str
    temperature: float
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class WeatherInDB(WeatherCreate):
    id: Optional[str] = None
