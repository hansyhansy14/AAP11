import urllib.request
import json

location = "Rietz, Tirol"
url = f"https://wttr.in/{location}?format=j1"

try:
    with urllib.request.urlopen(url) as response:
        json_string = response.read().decode('utf-8')  

    print("Full JSON string received:")
    print(json_string)

    weather_data = json.loads(json_string)

    current_conditions = weather_data["current_condition"][0]
    temperature = current_conditions["temp_C"]
    print(f"\nCurrent temperature in {location}: {temperature} °C")

except urllib.error.URLError as e:
    print("Error fetching weather data:", e)
