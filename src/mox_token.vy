# @pragma >= 0.4.0 

from snekmate.auth import ownable as ow 

initializes: ow 

@deploy 
def __init__():
    ow.__init__()

