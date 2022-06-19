# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use openweathermap.org
import requests

city = input("Enter your city: ")

base_url = "http://api.weatherapi.com/v1/current.json"
params = dict()
params["key"] = "bac8006360b7473eba0134824221906"
params["q"] = city
params['aqi'] = "no"

try:
    r = requests.get(url=base_url, params=params)
    data = r.json()
    print(
        f'{data["location"]["name"]}, {data["location"]["country"]}, {data["current"]["temp_c"]} °C, {data["current"]["condition"]["text"]}')
except KeyError:
    print("You have entered wrong city")