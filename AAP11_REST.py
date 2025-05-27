import requests
import json

location = "Rietz,Tirol"
url = f"https://wttr.in/{location}?format=j1"

try:
    response = requests.get(url)
    response.raise_for_status()  

    json_string = response.text

    print("Full JSON string received:")
    print(json_string)

    weather_data = json.loads(json_string)

    current_conditions = weather_data["current_condition"][0]
    temperature = current_conditions["temp_C"]

    print("-------------------------------------------------------------------------------------------")
    print(f"\nCurrent temperature in {location}: {temperature} °C")

except requests.exceptions.RequestException as e:
    print("-------------------------------------------------------------------------------------------")
    print("Error fetching weather data:", e)
