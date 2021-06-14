"""
Bernardo Paulsen

Exercise from class 359 from section 19
from Learn Complete Python In Simple Way.
"""
import logging

logging.basicConfig(filename="log359.txt",level=logging.WARNING)

logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")

