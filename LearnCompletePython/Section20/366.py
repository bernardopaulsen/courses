"""
Bernardo Paulsen

Exercise from class 366 from section 20
from Learn Complete Python In Simple Way.
"""
import logging

# Logger object

logger = logging.getLogger('demologer')
logger.setLevel(logging.WARNING)

# Handler object

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

fileHandler = logging.FileHandler("366.log", mode = "w")
fileHandler.setLevel(logging.ERROR)

# Formatter object

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d/%m/Y")

# set Formatter to Handler

consoleHandler.setFormatter(formatter)

# add Handler to Logger

logger.addHandler(consoleHandler)

# Execution

logger.critical("This is a critical message.")
logger.error("This is an error message.")
logger.warning("This is a warning message")
