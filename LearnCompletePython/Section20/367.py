"""
Bernardo Paulsen

Exercise from class 367 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

logger = logging.getLogger('demologer')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
fileHandler = logging.FileHandler("367.log", mode = "w")
fileHandler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d/%m/%Y")

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# Execution

logger.critical("This is a critical message.")
logger.error("This is an error message.")
logger.warning("This is a warning message.")
logger.info("This is an info message.")
logger.debug("This is a debug message.")
