from books_recommender.exception.exception_handler import AppException
from books_recommender.logger.log import logging
import sys

try: 
    logging.info('Trying to divide')
    a = 5/0
except Exception as e:
    raise AppException(e,sys)