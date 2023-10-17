from typing import Any

from aiogram.types import Message

from aiogram.filters.command import Command
from django.shortcuts import get_object_or_404

from apps.weather.models import City
from apps.weather.utils.integration import yandex_forecast_city
from tgbot.src.config.basic import dp, bot


async def main():
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Напишите название города, чтобы получить данные погоды ☁️")


@dp.message()
def message_handler(message: Message) -> Any:
    city_name = message.text
    try:
        weather_data = yandex_forecast_city(city_name)
        return message.answer(f"Город: {city_name}  🌇️️\n"
                              f"Температура: {weather_data.get('fact').get('temp')} C° 🌡️\n"
                              f"Давление: {weather_data.get('fact').get('pressure_mm')} мм рт.ст. 💎\n"
                              f"Скорость ветра: {weather_data.get('fact').get('wind_speed')} м/с 💨")
    except:
        return message.answer("Город не найден - 404 🚫")