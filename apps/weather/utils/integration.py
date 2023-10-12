from config.settings import YANDEX_API_KEY
import requests


def yandex_forecast():
    url = 'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU'

    headers = {
        "X-Yandex-API-Key": YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()
