# OpenNetAPI

### Select API

https://github.com/public-apis/public-apis

Option: https://openweathermap.org/

# 🌤 OpenWeather API 2.5 Testing

## 📌 Project Introduction
Using `pytest` to Execute API Testing for `OpenWeather API 2.5 + Geocoding API` 

## ✅ Test Cases
| Test Cases | Expected Result | Validation Method |
|--------|--------|--------|
| Search `Tokyo` Weather | HTTP 200 | `assert response.status_code == 200` |
| Search `New York` Weather | HTTP 200 | `assert response.status_code == 200` |
| Search Invalid City | HTTP 400 | `assert response.status_code == 400` |

## 📦 Execute API Testing
```bash
pytest -s
```

#### Current Weather Data
https://openweathermap.org/current
```
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
```
Free: 

60 calls/minute

1,000,000 calls/month
* Access current weather data for any location
* We collect and process weather data from different sources such as global and local weather models, satellites, radars and a vast network of weather stations
* JSON, XML, and HTML formats
* Included in both free and paid subscriptions

##### Geocoding API
https://openweathermap.org/api/geocoding-api
```
https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}
```

