import json

raw_response = '{"city": "Indore", "temperature": 34, "condition": "sunny", "humidity": 78, "wind": {"speed": 12, "unit": "kmh"}}'

data = json.loads(raw_response)

print(data["city"])
print(data["temperature"])
print(data["humidity"])
print(data["wind"]["speed"])

for key, value in data.items():
    print(f"{key} --> {value}")

print("\nWind details:")
for key, value in data["wind"].items():
    print(f"  {key}: {value}")

print(f"\nHumidity: {data['humidity']}")
