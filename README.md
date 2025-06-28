# Weather-Data-API

WeatherAPI – Agrégateur de Données Météorologiques
Ce projet est une API REST construite avec FastAPI qui agrège les données météo provenant de plusieurs services externes (Open-Meteo, OpenWeatherMap, WeatherAPI). Il a été développé dans une logique TDD avec tests d’intégration, de contrat, de charge et monitoring.

Fonctionnalités principales
[x] GET /weather/current/{city} : récupère la température actuelle d'une ville
[x] Agrégation multi-sources avec fallback intelligent
[x] Documentation Swagger automatique (/docs)
[x] Tests unitaires, d'intégration et de contrat avec pytest & jsonschema
[x] Test de charge avec Locust
[x] Monitoring Prometheus-compatible
Installation
git clone https://github.com/ahmeddogui/Weather-Data-API
cd WeatherAPI
pip install -r requirements.txt
Démarrage de l'API
uvicorn main:app --reload
Accessible ensuite sur : - Swagger : http://localhost:8000/docs - Endpoint santé : http://localhost:8000/health

Lancer les tests
# Tests unitaires et d'intégration
pytest

# Test de contrat
pytest src/tests/contract/test_weather_contract.py

# Test de charge
locust -f locustfile.py
Monitoring (optionnel)
L'API expose des métriques compatibles Prometheus via prometheus-fastapi-instrumentator.

Architecture du projet
weather_api/
├── src/
│   ├── controllers/
│   │   └── weather_controller.py
│   ├── services/
│   │   └── weather_service.py
│   └── tests/
│       ├── integration/
│       ├── contract/
├── main.py
├── requirements.txt
├── locustfile.py
Licence
MIT – Ce projet est libre de réutilisation avec attribution.
