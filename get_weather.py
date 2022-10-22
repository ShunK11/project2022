import requests
import json
import time

point = 'Toyota'

def return_weather():
    weather = {"sunny":["Clear"],"cloudy":["Clouds"],"rainy":["Rain","Thunderstorm","Drizzle","Snow"]}

    api_key = "f8d9753b7e9e7feb48f5f35dd8944d59"
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

    url = api.format(city = point, key = api_key)

    time.sleep(1)
    weather_data = requests.request("GET", url)
    weather_json = json.loads(weather_data.text)

    # print(weather_json)
    now_weather = weather_json['weather'][0]['main']

    for key in weather:
        if now_weather in weather[key]:
            now_weather = key
    return now_weather