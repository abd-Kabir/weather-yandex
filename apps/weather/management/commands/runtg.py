import asyncio

from django.core.management import BaseCommand

from tgbot.src.handlers.commands import main


class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **kwargs):
        asyncio.run(main())
