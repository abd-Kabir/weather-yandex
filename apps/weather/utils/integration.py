from config.settings import YANDEX_API_KEY
import requests


def yandex_forecast():
    url = 'https://api.weather.yandex.ru/v2/forecast?lang=ru_RU'

    headers = {
        "X-Yandex-API-Key": YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()


def list_of_cities():
    url = f"https://api.tickets.yandex.net/api/crm?action=crm.city.list&auth={YANDEX_API_KEY}"

    headers = {
        "X-Yandex-API-Key": YANDEX_API_KEY
    }

    resp = requests.get(url=url, headers=headers)
    return resp.json()
