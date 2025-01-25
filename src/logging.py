import logging


def setup_logging():
    logger = logging.getLogger('disnake')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    file_handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
