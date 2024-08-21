# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 23:52:03 2023

@author: PREKSHA
"""

import requests
import pyfiglet
from datetime import datetime
#import chalk

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Map weather codes to icons
WEATHER_ICONS = {
     "01d": "🌞", "02d": "🌤️", "03d": "☁", "04d": "🌥️", "09d": "🌧️",
     "10d": "🌦️", "11d": "⛈️", "13d": "❄️", "50d": "🌫️",
     "01n": "🌕", "02n": "🌑", "03n": "☁️", "04n": "🌥️", "09n": "🌧️",
     "10n": "🌦️", "11n": "⛈️", "13n": "❄️", "50n": "🌫️",
}

# Get city input from user
city_name = input("Enter the city to check the weather for: ")

# Construct API URL
url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

# Make API request and parse response
response = requests.get(url)
if response.status_code != 200:
    print("Error: unable to retrieve weather info")
    exit()

# Parse JSON from API and extract info
data = response.json()

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
visibility = data.get("visibility", "N/A")
wind_speed = data["wind"]["speed"]
desc = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Convert sunrise and sunset times to human-readable format
sunrise_timestamp = data["sys"]["sunrise"]
sunset_timestamp = data["sys"]["sunset"]
sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = datetime.utcfromtimestamp(sunset_timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Construct output with icons and format
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"Weather: {desc} {weather_icon}\n"
output += f"Temperature: {temp} C         Feels_like: {feels_like} C\n"
output += f"Min Temperature: {temp_min} C     Max Temperature: {temp_max} C\n"
output += f"Pressure: {pressure} hPa           Humidity: {humidity}%\n"
output += f"Visibility: {visibility} meters     Wind Speed: {wind_speed} m/s\n"
output += f"Sunrise time: {sunrise_time} hrs\n"
output += f"Sunset time: {sunset_time} hrs"

print(output)
















