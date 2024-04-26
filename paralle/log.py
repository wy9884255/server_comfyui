import logging
import datetime
from logging.handlers import TimedRotatingFileHandler
class Log:
    def __init__(self):
        path = f"/home/wy/server_comfyui/log/paralle.log"
        handler = TimedRotatingFileHandler(path, when='midnight')
        logging.basicConfig(handlers=[handler], level=logging.INFO)

    def output_logs(self, message, prefix="[NORMAL]"):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{current_time}: {prefix}{message}")