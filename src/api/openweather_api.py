import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class OpenWeatherAPI:
    BASE_URL_GEOCODING = "https://api.openweathermap.org/geo/1.0/direct"
    BASE_URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_lat_lon(city):
        """Get Lat and Lon By City Name"""
        api_key = os.getenv("OPENWEATHER_API_KEY")
        params = {"q": city, "limit": 1, "appid": api_key}
        print('GET', OpenWeatherAPI.BASE_URL_GEOCODING, params)
        response = requests.get(
            OpenWeatherAPI.BASE_URL_GEOCODING, params=params)

        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return data["lat"], data["lon"]
        else:
            raise ValueError(
                f"Unable to get lat and lon of City: {city} , error {response.json()}")

    @staticmethod
    def get_weather_by_city(city):
        """Get Weather by City via Current Weather API"""
        lat, lon = OpenWeatherAPI.get_lat_lon(city)
        api_key = os.getenv("OPENWEATHER_API_KEY")

        params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
        print('GET', OpenWeatherAPI.BASE_URL_WEATHER, params)
        response = requests.get(OpenWeatherAPI.BASE_URL_WEATHER, params=params)
        return response
