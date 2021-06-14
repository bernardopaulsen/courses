"""
Bernardo Paulsen

Exercise from class 362 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s:%(lineno)s:%(funcName)s:%(module)s")

logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")