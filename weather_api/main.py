from fastapi import FastAPI
from src.controllers.weather_controller import router as weather_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de Données Météo")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route météo avec préfixe /weather
app.include_router(weather_router, prefix="/weather")

@app.get("/health")
def health():
    return {"status": "ok"}
