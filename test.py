import sys

from src.logger.logger import logging
from src.exception.custom_exception import CustomException


try:
    a = 1 / 0

except Exception as e:
    logging.error(e)
    raise CustomException(e, sys)