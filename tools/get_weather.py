import json
import urllib.request
import urllib.parse
import urllib.error

def get_weather(city, units="celsius"):
    """
    Fetches real weather data using the free Open-Meteo API (no API key required).
    """
    try:
        # 1. Look up the coordinates for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(city)}&count=1&language=en&format=json"
        
        req = urllib.request.Request(geo_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            geo_data = json.loads(response.read())
            
        if not geo_data.get("results"):
            return f"Error: Could not find coordinates for city '{city}'."
            
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        resolved_name = geo_data["results"][0]["name"]
        
        # 2. Fetch the current weather for those coordinates
        unit_str = "" if units == "celsius" else "&temperature_unit=fahrenheit"
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true{unit_str}"
        
        req = urllib.request.Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            weather_data = json.loads(response.read())
            
        current = weather_data["current_weather"]
        temp = current["temperature"]
        
        return f"The current temperature in {resolved_name} is {temp}° {units.capitalize()}."
        
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
