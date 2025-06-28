from locust import HttpUser, task, between
import random

class WeatherAPIUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def get_current_weather(self):
        cities = ["Paris", "London", "Tokyo", "New York", "Madrid"]
        city = random.choice(cities)
        self.client.get(f"/weather/current/{city}")

    @task(1)
    def health_check(self):
        self.client.get("/health")
