import requests
from datetime import datetime
from django.shortcuts import render

API_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_PARAMS = {"latitude":41.8781,
                  "longitude":-87.6298,
                  "current":"temperature_2m, wind_speed_10m",
                  "daily":"temperature_2m_max, temperature_2m_min, precipitation_sum",
                  "timezone":"America/Chicago"
                  }

# Create your views here.
def weather_page(request):
    error = None
    bullets = []
    
    try:
        response = requests.get(API_URL, params=DEFAULT_PARAMS, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        error = "Unable to connect to the weather service. Please try again later."
        data = None

    if data:
        # Safely get current weather data
        current = data.get("current", {})
        current_temp = current.get('temperature_2m')
        wind_speed = current.get('wind_speed_10m')

        # Safely get daily weather data ( it's in a list )
        daily = data.get('daily',{})
        temp_max = daily.get('temperature_2m_max', [None])[0]
        temp_min = daily.get('temperature_2m_min', [None])[0]
        precipitation = daily.get('precipitation_sum', [None])[0]

        # Format into human-readable strings, checking if data exists
        if current_temp is not None:
            bullets.append(f"Current temperature: {current_temp}°C")

        if wind_speed is not None:
            bullets.append(f"Current wind speed: {wind_speed} km/h")
        if temp_max is not None:
            bullets.append(f"Today's high: {temp_max}°C")
        if temp_min is not None:
            bullets.append(f"Today's low: {temp_min}°C")
        if precipitation is not None:
            bullets.append(f"Today's precipitation: {precipitation} mm")

        context = {
            "title" : "Chicago Weather",
            "bullets": bullets,
            "error": error,
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    return render(request, "weather/weather.html", context)