# @pragma >= 0.4.0 

# -- Imports -- #
from snekmate.auth import ownable as ow 
from snekmate.tokens import erc20
from ethereum.ercs import IERC20 

# -- Implementations -- #
implements: IERC20

# -- Initiliazers -- #
initializes: ow 
initializes: erc20[ownable := ow]

# -- Exports -- #
exports: (erc20.__interface__)

# -- Errors -- #
ERROR_NOT_OWNER: public(constant(String[70])) = "Modafucka, you are not the owner!!!"
ERROR_NO_ZERO: public(constant(String[70])) = "Cannot increase/decrease to modafuckin zero!!!"
ERROR_CAN_NOT: public(constant(String[70])) = "Cannot increase/decrease to the modafuckin current max supply!!!"

# -- Storage -- #
NAME: constant(String[25]) = "Mox_Token"
SYMBOL : constant(String[5]) = "$mxtk"
DECIMALS: constant(uint8) = 18
# EIP_NAME: constant(String[50]) = "Mox_Token"
EIP_VERSION: constant(String[20]) = "1"
MAX_SUPPLY: uint256
OWNER: immutable(address)


# -- Constructor -- #
@deploy 
def __init__(max_supply: uint256):
    ow.__init__()
    erc20.__init__(NAME, SYMBOL, DECIMALS, NAME, EIP_VERSION)
    self.MAX_SUPPLY = max_supply
    OWNER = msg.sender


# -- Modifers -- #
@internal 
def _only_owner():
    assert msg.sender == OWNER, ERROR_NOT_OWNER


# -- External Defs -- #
@external 
def increase_max_supply(new_max_supply: uint256):
    self._only_owner()
    assert new_max_supply != 0, ERROR_NO_ZERO
    assert new_max_supply != self.MAX_SUPPLY, ERROR_CAN_NOT
    self.MAX_SUPPLY = new_max_supply 

@external 
def decrease_max_supply(new_max_supply: uint256):
    self._only_owner()
    assert new_max_supply != 0, ERROR_NO_ZERO
    assert new_max_supply != self.MAX_SUPPLY, ERROR_CAN_NOT
    self.MAX_SUPPLY = new_max_supply


# -- Getter Defs -- #
@external 
@view 
def get_max_supply() -> uint256:
    return self.MAX_SUPPLY

