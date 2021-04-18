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

# Load JSON data into a Python variable.
weather_data = json.loads(response.text)

# Print weather descriptions.
w = weather_data['list']
print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])