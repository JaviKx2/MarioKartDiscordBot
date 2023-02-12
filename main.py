import os


from src.Bot import bot
from src.logging import setup_logging


setup_logging()
bot.run(
    os.getenv(
        'MARIOKART_BOT_TOKEN',
        default=""
    )
)
