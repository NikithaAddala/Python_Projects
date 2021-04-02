import requests
from pprint import pprint

API_Key = 'fdac4f322c31b5947f382c81a87bfed9'

city = input("Enter city name: ")
base_url = "https://home.openweathermap.org/api_keys?appid="+API_Key+"&q="+city
weather_data = requests.get(base_url).jason()

pprint(weather_data)