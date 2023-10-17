from rest_framework.generics import get_object_or_404

from apps.weather.models import City
from django.conf import settings
import requests


def yandex_forecast_coordination(lat, lon):
    url = f'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU&lat={lat}&lon={lon}'

    headers = {
        "X-Yandex-API-Key": settings.YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()


def yandex_forecast_city(city):
    city = city.capitalize()
    city = get_object_or_404(City, name__icontains=city)
    lat = city.lat
    lon = city.lon

    url = f'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU&lat={lat}&lon={lon}'

    headers = {
        "X-Yandex-API-Key": settings.YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()
