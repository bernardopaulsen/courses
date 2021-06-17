"""
Bernardo Paulsen

Exercise from class 370 from section 20
from Learn Complete Python In Simple Way.
"""
import inspect
import logging

def get_custom_logger(level):
    function_name= inspect.stack()[1][3]
    logger_name = function_name + " logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    fileHandler = logging.FileHandler("370.log", mode = "a")
    fileHandler.setLevel(level)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s", datefmt="%d/%m/%Y %i:%M:%S")
    
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger