import requests
from jsonschema import validate

weather_schema = {
    "type": "object",
    "required": ["city", "temperature", "sources"],
    "properties": {
        "city": {"type": "string"},
        "temperature": {
            "type": "object",
            "required": ["current", "unit"],
            "properties": {
                "current": {"type": "number"},
                "unit": {"type": "string"}
            }
        },
        "sources": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1
        }
    }
}

def test_weather_response_schema():
    city = "Paris"
    url = f"http://localhost:8000/weather/current/{city}"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    # 💡 Validation du contrat
    validate(instance=data, schema=weather_schema)
