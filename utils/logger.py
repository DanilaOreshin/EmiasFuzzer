import logging

from utils.config import log_level, logger_message_format, logger_file_name

logging.basicConfig(level=log_level,
                    format=logger_message_format,
                    handlers=[
                        logging.FileHandler(logger_file_name),
                        logging.StreamHandler()]
                    )

logger = logging.getLogger()
