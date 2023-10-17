from rest_framework.generics import get_object_or_404

from apps.weather.models import City
from django.conf import settings
import requests

from config.utils.api_exceptions import APIValidation


def yandex_forecast_coordination(lat, lon):
    url = f'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU&lat={lat}&lon={lon}'

    headers = {
        "X-Yandex-API-Key": settings.YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()


def yandex_forecast_city(city_name):
    cities = City.objects.all()

    city_name = city_name.replace("_", "").replace("-", "").replace(" ", "")
    city_name = city_name.capitalize()
    # city = get_object_or_404(City, name__istartswith=city_name)
    filtered_cities = [city for city in cities if city.name.lower().startswith(city_name.lower())]
    if filtered_cities:
        lat = filtered_cities[0].lat
        lon = filtered_cities[0].lon

        url = f'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU&lat={lat}&lon={lon}'

        headers = {
            "X-Yandex-API-Key": settings.YANDEX_API_KEY
        }

        resp = requests.get(url=url, headers=headers)
        return resp.json()
    else:
        raise APIValidation("Город не найден")
