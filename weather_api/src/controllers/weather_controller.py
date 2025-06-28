from fastapi import APIRouter, HTTPException
from src.services.weather_service import WeatherService

router = APIRouter()
weather_service = WeatherService()

@router.get("/current/{city}")
async def get_current_weather(city: str):
    print("📍 Reçu une requête pour la ville :", city)

    if not city:
        raise HTTPException(status_code=400, detail="City parameter is required")

    data = weather_service.get_current_weather(city)

    if data is None:
        raise HTTPException(status_code=404, detail="City not found")

    return data
