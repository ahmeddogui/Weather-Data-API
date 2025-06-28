import requests
import os

class WeatherService:
    def __init__(self):
        self.open_meteo_url = "https://api.open-meteo.com/v1/forecast"
        self.openweather_url = "https://api.openweathermap.org/data/2.5/weather"
        self.weatherapi_url = "https://api.weatherapi.com/v1/current.json"

        self.openweather_key = os.getenv("OPENWEATHER_API_KEY")
        self.weatherapi_key = os.getenv("WEATHERAPI_KEY")

    def get_city_coordinates(self, city):
        city = city.capitalize()  # 🔥 Corrige les majuscules/minuscules

        coords = {
            "Paris": (48.8566, 2.3522),
            "London": (51.5074, -0.1278),
            "Tokyo": (35.6762, 139.6503),
            "New York": (40.7128, -74.0060),
            "Madrid": (40.4168, -3.7038),
        }
        return coords.get(city)


    def get_open_meteo_weather(self, city):
        coords = self.get_city_coordinates(city)
        if not coords:
            return None

        lat, lon = coords
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        try:
            response = requests.get(self.open_meteo_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return {
                    "source": "open-meteo",
                    "temperature": data["current_weather"]["temperature"],
                    "unit": "celsius"
                }
        except:
            return None

        return None

    def get_openweather_weather(self, city):
        if not self.openweather_key:
            return None

        params = {
            "q": city,
            "appid": self.openweather_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.openweather_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return {
                    "source": "openweather",
                    "temperature": data["main"]["temp"],
                    "unit": "celsius"
                }
        except:
            return None

        return None

    def get_weatherapi_weather(self, city):
        if not self.weatherapi_key:
            return None

        params = {
            "key": self.weatherapi_key,
            "q": city,
            "aqi": "no"
        }

        try:
            response = requests.get(self.weatherapi_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return {
                    "source": "weatherapi",
                    "temperature": data["current"]["temp_c"],
                    "unit": "celsius"
                }
        except:
            return None

        return None

    def get_current_weather(self, city):
        sources = [
            self.get_open_meteo_weather(city),
            self.get_openweather_weather(city),
            self.get_weatherapi_weather(city)
        ]

        valid_data = [s for s in sources if s]

        if not valid_data:
            return None

        avg_temp = sum([d["temperature"] for d in valid_data]) / len(valid_data)
        return {
            "city": city,
            "temperature": {
                "current": round(avg_temp, 1),
                "unit": "celsius"
            },
            "sources": [d["source"] for d in valid_data]
        }
