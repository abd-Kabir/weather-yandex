import logging

from aiogram import Bot, Dispatcher
from tgbot.src.config import TG_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
