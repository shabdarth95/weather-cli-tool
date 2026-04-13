# Weather CLI Tool

A command-line tool that fetches real-time weather data for any city
using a live API and saves the results locally.

## What it does
- Takes a city name as user input
- Calls the wttr.in weather API
- Displays temperature, humidity, wind speed, UV index, sunrise and sunset
- Saves the raw weather data as a JSON file

## What I learned building this
- How REST APIs work and how to call them with Python
- How to parse and navigate nested JSON responses
- How to structure code into single-responsibility functions
- How to handle API errors using status codes
- How to save data to files using Python

## How to run it

Make sure you have Python 3 and requests installed:

pip3 install requests

Then run:

python3 weather_tool.py

Enter any city name when prompted.

## Example output

===================================
  Weather for INDORE
===================================
  Temperature  : 36°C
  Feels like   : 35°C
  Condition    : Sunny
  Humidity     : 21%
  Wind speed   : 9 kmph
  UV Index     : 10
  Sunrise