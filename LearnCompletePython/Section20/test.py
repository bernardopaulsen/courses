"""
Bernardo Paulsen

Exercise from class 370 from section 20
from Learn Complete Python In Simple Way.
"""
from customlogger import get_custom_logger
import logging

def f1():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("This is a critical message.")
    logger.error("This is a error message.")
    logger.warning("This is a warning message.")
    logger.info("This is a info message.")
    logger.debug("This is a debug message.")

def f2():
    logger = get_custom_logger(logging.WARNING)
    logger.critical("This is a critical message.")
    logger.error("This is a error message.")
    logger.warning("This is a warning message.")
    logger.info("This is a info message.")
    logger.debug("This is a debug message.")

f1()
f2()