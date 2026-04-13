import requests
import json
from datetime import datetime

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Could not get weather for {city}")
        return None
    
    return response.json()

def display_weather(data, city):
    current = data["current_condition"][0]
    today = data["weather"][0]
    astro = today["astronomy"][0]
    
    print(f"\n{'='*35}")
    print(f"  Weather for {city.upper()}")
    print(f"{'='*35}")
    print(f"  Temperature  : {current['temp_C']}°C")
    print(f"  Feels like   : {current['FeelsLikeC']}°C")
    print(f"  Condition    : {current['weatherDesc'][0]['value']}")
    print(f"  Humidity     : {current['humidity']}%")
    print(f"  Wind speed   : {current['windspeedKmph']} kmph")
    print(f"  UV Index     : {current['uvIndex']}")
    print(f"  Sunrise      : {astro['sunrise']}")
    print(f"  Sunset       : {astro['sunset']}")
    print(f"  Moonrise     : {astro['moonrise']}")
    print(f"{'='*35}\n")

def save_to_file(data, city):
    filename = f"{city}_weather.json"
    with open(filename, "w") as f:
        json.dump(data["current_condition"][0], f, indent=2)
    print(f"  Data saved to {filename}")

# --- Main program ---
city = input("Enter city name: ")
print(f"Fetching weather for {city}...")

data = get_weather(city)

if data:
    display_weather(data, city)
    save_to_file(data, city)