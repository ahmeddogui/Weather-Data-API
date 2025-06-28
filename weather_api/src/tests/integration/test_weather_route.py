import requests

def test_get_current_weather():
    city = "Paris"
    url = f"http://localhost:8000/weather/current/{city}"

    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} with body {response.text}"

    data = response.json()
    assert data["city"] == city
    assert "temperature" in data
    assert "current" in data["temperature"]
    assert "unit" in data["temperature"]
    assert isinstance(data["temperature"]["current"], (float, int))
    assert "sources" in data
    assert isinstance(data["sources"], list)
    assert len(data["sources"]) >= 1
