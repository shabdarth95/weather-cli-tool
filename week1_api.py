import json
import requests

url = "https://wttr.in/Indore?format=j1"

print("Calling the API...")
response = requests.get(url)

print(f"Status code: {response.status_code}")

data = response.json()

current = data["current_condition"][0]
today_weather = data["weather"][0]

print(f"\nCity: Indore")
print(f"Temperature: {current['temp_C']}°C")
print(f"Feels like: {current['FeelsLikeC']}°C")
print(f"Condition: {current['weatherDesc'][0]['value']}")
print(f"Humidity: {current['humidity']}%")
print(f"Wind speed: {current['windspeedKmph']} kmph")
print(f"Sunset time: {today_weather['astronomy'][0]['sunset']}")

print("\n--- RAW RESPONSE SAMPLE ---")
print(json.dumps(data["current_condition"][0], indent=2))
# Map the full structure before extracting anything
print("\n--- STRUCTURE EXPLORER ---")
print("Top level keys:", list(data.keys()))
print("current_condition type:", type(data["current_condition"]))
print("current_condition[0] type:", type(data["current_condition"][0]))
print("current_condition[0] keys:", list(data["current_condition"][0].keys()))
print("weather type:", type(data["weather"]))
print("weather[0] keys:", list(data["weather"][0].keys()))
print("astronomy[0] keys:", list(data["weather"][0]["astronomy"][0].keys()))