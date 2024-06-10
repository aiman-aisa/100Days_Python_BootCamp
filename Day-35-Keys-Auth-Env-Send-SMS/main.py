
from config import api_key, twilio_sid, twilio_auth_token
import requests
from twilio.rest import Client

parameters = {
    "lat": 2.961015,
    "lon": 101.795743,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
# print(response.json())

weather_data = response.json()["list"]
# print(weather_data)

will_rain = False

for value in weather_data:
    condition_code = value['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an umbrella!",
        from_ = "+17012531948",
        to = "+60194745451"
    )
    print(message.status)
    


