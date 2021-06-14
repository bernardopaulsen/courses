"""
Bernardo Paulsen

Exercise from class 363 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%d/%m/%Y %H:%M:%S")

logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")
