WeatherAPI – Weather Data Aggregator
This project is a REST API built with FastAPI that aggregates weather data from multiple external services (Open-Meteo, OpenWeatherMap, WeatherAPI). It was developed following a TDD approach and includes integration, contract, load testing, and monitoring.

🚀 Main Features
 GET /weather/current/{city}: Fetches the current temperature of a given city

 Multi-source aggregation with intelligent fallback

 Auto-generated Swagger documentation at /docs

 Unit, integration, and contract testing with pytest & jsonschema

 Load testing using Locust

 Prometheus-compatible monitoring

📦 Installation
bash
Copier
Modifier
git clone https://github.com/ahmeddogui/Weather-Data-API.git
cd WeatherAPI
pip install -r requirements.txt
▶️ Running the API
bash
Copier
Modifier
uvicorn main:app --reload
Accessible at:

Swagger UI: http://localhost:8000/docs

Health check: http://localhost:8000/health

✅ Running Tests
Unit and Integration Tests
bash
Copier
Modifier
pytest
Contract Test
bash
Copier
Modifier
pytest src/tests/contract/test_weather_contract.py
Load Testing
bash
Copier
Modifier
locust -f locustfile.py
📈 Monitoring (Optional)
The API exposes Prometheus-compatible metrics using prometheus-fastapi-instrumentator.

🧱 Project Structure
```text
weather_api/
├── captures/
├── src/
│   ├── controllers/
│   │   └── weather_controller.py
│   ├── services/
│   │   └── weather_service.py
│   └── tests/
│       ├── integration/
│       └── contract/
├── main.py
├── requirements.txt
├── locustfile.py
├── docker-compose.yml

```
📄 License
MIT – This project is open-source and free to use with attribution.

