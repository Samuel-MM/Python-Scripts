import requests

API_KEY='enteryourapikey' # Insert your api key
CITY_NAME='São Paulo' # Change the city name
URL='http://api.weatherapi.com/v1/forecast.json'

params={'key': API_KEY, 'q': CITY_NAME}

response = requests.get(URL, params).json()

# Getting data
localtime = response['location']['localtime']
condition = response['current']['condition']['text']
temperature = response['current']['temp_c']
humidity = response['current']['humidity']
rainChance = response['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
totalPrecipitation = response['forecast']['forecastday'][0]['day']['totalprecip_mm']
uv = response['forecast']['forecastday'][0]['day']['uv']

# Showing data
print(
    f'City: {CITY_NAME}, \n'
    f'Localtime: {localtime}, \n'
    f'condition: {condition}, \n'
    f'temperature (ºC): {temperature}, \n'
    f'humidity: {humidity}, \n'
    f'rain chance: {rainChance}, \n'
    f'total precipitation (mm): {totalPrecipitation}, \n'
    f'uv: {uv}'
)
