import pytest
from src.api.openweather_api import OpenWeatherAPI


@pytest.mark.parametrize("city, expected_status", [
    ("Tokyo", 200),
    ("New York", 200),
    ("InvalidCity12345", 400),  # 反向測試
])
def test_openweather_api(city, expected_status):
    """Test OpenWeather API 2.5 Support City Name search"""
    if expected_status == 200:
        response = OpenWeatherAPI.get_weather_by_city(city)
        assert response.status_code == 200, f"Expected {expected_status}, got {response.status_code}"

        data = response.json()
        assert "weather" in data, "Fail: API response not contain 'weather'"
        assert "temp" in data["main"], "Fail: API response miss 'temp'"
        assert "humidity" in data["main"], "Fail: API response miss 'humidity'"
        assert "pressure" in data["main"], "Fail: API response miss 'pressure'"
    else:
        with pytest.raises(ValueError):
            OpenWeatherAPI.get_lat_lon(city)
