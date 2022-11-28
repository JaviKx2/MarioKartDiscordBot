import os

from dotenv import load_dotenv


print(load_dotenv())


print(os.getenv("MARIOKART_BOT_TOKEN"))
print(os.getenv("PG_CONN_URL"))

