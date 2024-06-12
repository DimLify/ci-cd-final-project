import logging
from logging.handlers import RotatingFileHandler
import os

def init_logging(app, log_name):
    """Initialize logging configuration"""
    log_level = logging.INFO

    if not os.path.exists("logs"):
        os.mkdir("logs")
    
    file_handler = RotatingFileHandler(f"logs/{log_name}.log", maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))
    file_handler.setLevel(log_level)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)
    app.logger.info("Logging is set up.")
