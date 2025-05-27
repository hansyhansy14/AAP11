# Weather Fetcher with Python

This repository contains two Python scripts that fetch and display the current temperature for a specified location using the [wttr.in](https://wttr.in) weather service API.

---

## Scripts Overview

### 1. `weather_urllib.py`

This script uses Python's built-in `urllib` library to perform an HTTP GET request and fetch weather data in JSON format.

- Uses `urllib.request` to retrieve data.
- Decodes and prints the full JSON response.
- Parses the JSON to extract and print the current temperature in Celsius.
- Handles URL errors gracefully.

### 2. `weather_requests.py`

This script uses the popular third-party `requests` library for HTTP requests.

- Uses `requests.get()` to fetch data.
- Prints the full JSON response.
- Parses the JSON to extract and print the current temperature in Celsius.
- Handles HTTP and network exceptions gracefully.

---

## Usage

1. Make sure you have Python 3 installed.

2. For the `weather_requests.py` script, install the `requests` library if you haven't already:

   ```bash
   pip install requests
