from src import app_properties
from src.Bot import bot
from src.logging import setup_logging

setup_logging()
bot.run(app_properties.MARIOKART_BOT_TOKEN)
