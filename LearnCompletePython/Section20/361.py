"""
Bernardo Paulsen

Exercise from class 361 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

logging.basicConfig(filename="log361.txt",level=logging.DEBUG,filemode="w")

logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")