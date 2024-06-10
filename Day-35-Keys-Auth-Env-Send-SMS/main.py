
from secrets import api_key
import requests

parameters = {
    "lat": 2.961015,
    "lon": 101.795743,
    "app_id": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response)
response.raise_for_status()
