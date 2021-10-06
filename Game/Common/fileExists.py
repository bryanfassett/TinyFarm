from os.path import exists
from Game.Common import Throw

## Function to check if file exists and throw if not
# ## Parameters:
## path = path to file
## must_raise (optional) = if set true, raise an unhandled exception
def fileExists(path,must_raise = False):
    if not exists(path):
        if must_raise:
            raise FileNotFoundError(f"FileNotFoundError: {path}")
        else:
            try:
                raise FileNotFoundError(f"FileNotFoundError: {path}")
            except FileNotFoundError as e:
                Throw(e,False)
                return False
    else:
        return True