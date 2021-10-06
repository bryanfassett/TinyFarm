from Game.Common import Logger

## throw function will always log and print data. Primarily used for exceptions or important events
## Will throw exception by default, set to false if manually handling exception elsewhere
def Throw(data, handle = True):
    if handle:
        try:
            raise Exception(data)
        except Exception as e:
            data = e
    
    Logger.LogF(data)