from flask import Flask

from src import app_properties
from src.Bot import bot
from src.logging import setup_logging

flask_app = Flask(__name__)


@flask_app.route('/')
def root():
    return "I'm alive!"


def run():
    flask_app.run(host='0.0.0.0', port=8080)


def keep_alive():
    from threading import Thread
    t = Thread(target=run)
    t.start()


keep_alive()
setup_logging()
bot.run(app_properties.MARIOKART_BOT_TOKEN)
