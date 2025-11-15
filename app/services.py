import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    
def get_city_suggestions(query):
    base_url = "http://api.openweathermap.org/geo/1.0/direct?"
    url = f"{base_url}q={query}&limit=5&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching city suggestions: {e}")
        return None