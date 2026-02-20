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
    try:
        response = requests.get(API_URL, params=DEFAULT_PARAMS, timeout=10)
    except:
        pass

    return