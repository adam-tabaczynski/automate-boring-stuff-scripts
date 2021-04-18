#! python3
# get_open_weeather.py - Prints hte weather for a location
# from the command line.

import json, requests, sys

api_file = open('./app_id.txt')
api_key = api_file.read()

# Compute location from cmd.
if len(sys.argv) < 2:
  print('Usage: get_open_weather.py city_name')
  sys.exit()
  
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s' % (location, api_key)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.text)