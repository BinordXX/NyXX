import logging
from logging.handlers import RotatingFileHandler

# Define the log file location and max size before rotating logs
LOG_FILE = "nyxx_log.log"
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB
LOG_BACKUP_COUNT = 5  # Keep 5 backup copies of the log file

# Setting up the logger
def setup_logger():
    # Create a logger instance
    logger = logging.getLogger("NyXXLogger")
    
    # Set the minimum level of log messages (INFO, DEBUG, ERROR, etc.)
    logger.setLevel(logging.DEBUG)

    # Create a console handler for logging to console (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set console log level to INFO

    # Create a rotating file handler for logging to a file
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT)
    file_handler.setLevel(logging.DEBUG)  # Log all levels to the file, including DEBUG

    # Create a log formatter
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Attach the formatter to the handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Example logger instance
logger = setup_logger()

# Optionally, write some initial log messages (you can remove these later)
logger.info("Logger initialized and ready.")
