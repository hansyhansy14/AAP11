import requests
import json

location = "Rietz"
url = f"https://wttr.in/{location}?format=j1"

try:
    response = requests.get(url)
    response.raise_for_status()

    weather_data = response.json()

    current_conditions = weather_data["current_condition"][0]
    temperature = current_conditions["temp_C"]
    weather_description = current_conditions["weatherDesc"][0]["value"]
    humidity = current_conditions["humidity"]
    wind_speed = current_conditions["windspeedKmph"]

    print(f"Weather in {location}:")
    print(f"- Temperature: {temperature} °C")
    print(f"- Description: {weather_description}")
    print(f"- Humidity: {humidity}%")
    print(f"- Wind: {wind_speed} km/h")

except requests.exceptions.RequestException as e:
    print("Error retrieving weather data:", e)
