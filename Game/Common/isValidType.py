from Game.Common import *
from Game.Common.Throw import Throw

## Function to repeat this commonly used type validation pattern and throw if error
## Parameters:
## data = any data to compare type
## compare = example of type to compare
## must_raise (optional) = if set true, raise an unhandled exception
def isValidType(data,compare,must_raise = False):
    if not type(data) == type(compare):
        if must_raise:
            raise TypeError(f"TypeError: Invalid type provided: Expected {type(compare)}, Received {type(data)}")
        else:
            try:
                raise TypeError(f"TypeError: Invalid type provided: Expected {type(compare)}, Received {type(data)}")
            except TypeError as e:
                Throw(e)
                return False
    else:
        return True