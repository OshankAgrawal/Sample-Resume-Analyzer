import sys

from src.logger.logger import logger
from src.exception.custom_exception import CustomException


try:
    a = 1 / 0

except Exception as e:
    logger.error(e)
    raise CustomException(e, sys)