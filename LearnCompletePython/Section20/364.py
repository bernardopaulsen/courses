"""
Bernardo Paulsen

Exercise from class 364 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

logging.basicConfig(level=logging.INFO)

logging.info('New request.')
try:
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))
    print(a/b)
except ZeroDivisionError as msg:
    logging.exception(msg)
    print('Cannot divide by 0.')
except ValueError as msg:
    logging.exception(msg)
    print('Provide integers only.')
logging.info('Request completed.')