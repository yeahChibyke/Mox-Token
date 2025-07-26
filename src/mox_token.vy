# @pragma >= 0.4.0 

# -- IMPORTS -- #
from snekmate.auth import ownable as ow 
from snekmate.tokens import erc20
from ethereum.ercs import IERC20 

# -- IMPLEMENTATIONS -- #
implements: IERC20

# -- INITIALIZERS -- #
initializes: ow 
initializes: erc20[ownable := ow]


# -- EXPORTS -- #
exports: (erc20.__interface__)


# -- ERRORS -- #
ERROR_NOT_OWNER: public(constant(String[70])) = "Modafucka, you are not the owner!!!"
ERROR_NO_ZERO: public(constant(String[70])) = "Cannot increase/decrease to modafuckin zero!!!"
ERROR_CAN_NOT: public(constant(String[70])) = "Cannot increase/decrease to the modafuckin current max supply!!!"

# -- EVENTS -- #
event MaxSupplyIncreased:
    previous_max: indexed(uint256)
    new_max: indexed(uint256) 
    caller: address 

event MaxSupplyDecreased:
    previous_max: indexed(uint256) 
    new_max: indexed(uint256) 
    caller: address 


# -- STORAGE -- #
NAME: constant(String[25]) = "Mox_Token"
SYMBOL : constant(String[5]) = "$mxtk"
DECIMALS: constant(uint8) = 18
# EIP_NAME: constant(String[50]) = "Mox_Token"
EIP_VERSION: constant(String[20]) = "1"
MAX_SUPPLY: uint256
OWNER: immutable(address)


# -- CONSTRUCTOR -- #
@deploy 
def __init__(max_supply: uint256):
    ow.__init__()
    erc20.__init__(NAME, SYMBOL, DECIMALS, NAME, EIP_VERSION)
    self.MAX_SUPPLY = max_supply
    OWNER = msg.sender


# -- MODIFIERS -- #
@internal 
def _only_owner():
    assert msg.sender == OWNER, ERROR_NOT_OWNER


# -- EXTERNAL DEFS -- #
@external 
def increase_max_supply(new_max_supply: uint256):
    self._only_owner()
    assert new_max_supply != 0, ERROR_NO_ZERO
    assert new_max_supply != self.MAX_SUPPLY, ERROR_CAN_NOT

    previous_max_supply: uint256 = self.MAX_SUPPLY
    self.MAX_SUPPLY = new_max_supply 

    log MaxSupplyIncreased(
        previous_max=previous_max_supply, 
        new_max=new_max_supply, 
        caller=msg.sender
    )

@external 
def decrease_max_supply(new_max_supply: uint256):
    self._only_owner()
    assert new_max_supply != 0, ERROR_NO_ZERO
    assert new_max_supply != self.MAX_SUPPLY, ERROR_CAN_NOT

    previous_max_supply: uint256 = self.MAX_SUPPLY
    self.MAX_SUPPLY = new_max_supply

    log MaxSupplyDecreased(
        previous_max=previous_max_supply, 
        new_max=new_max_supply, 
        caller=msg.sender
    )


# -- GETTER DEFS -- #
@external 
@view 
def get_max_supply() -> uint256:
    return self.MAX_SUPPLY

