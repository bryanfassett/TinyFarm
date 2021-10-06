from Game.config import DETAILED_LOGGING
from Game.config import *

## log and print only if detailed logging is on
def Log(data):
    if DETAILED_LOGGING:
        print(data)
        _logger(data)

## force log, but only print if detailed logging is on
def LogF(data):
    _logger(data)
    if DETAILED_LOGGING:
        print(data)

## internal function to handle the logging of data to a log file
def _logger(data):
    pass ## TODO: Logger