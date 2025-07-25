# -- Imports -- #
import boa 
from eth_utils import to_wei

# -- Variables -- #
SMS = to_wei(1000, "ether") # Starting Max Supply
IMS = to_wei(5000, "ether") # Increased Max Supply
DMS = to_wei(100, "ether") # Decreased Max Supply


# -- Tests -- #

def test_owner(mox, owner):
    assert mox.owner() == owner.address

def test_max_supply(mox):
    assert mox.get_max_supply() ==  SMS

def test_increase_max_supply(mox, owner):
    with boa.env.prank(owner.address):
        mox.increase_max_supply(IMS)
    assert mox.get_max_supply() == IMS

def test_decrease_max_supply(mox, owner):
    with boa.env.prank(owner.address):
        mox.decrease_max_supply(DMS)
    assert mox.get_max_supply() == DMS


# -- Reverts -- #

def test_cannot_increase_max_supply_to_zero(mox, owner):
    with boa.env.prank(owner.address):
        with boa.reverts(mox.ERROR_NO_ZERO()):
            mox.increase_max_supply(0)

def test_cannot_increase_max_supply_to_current_max_supply(mox, owner):
    with boa.env.prank(owner.address):
        with boa.reverts(mox.ERROR_CAN_NOT()):
            mox.increase_max_supply(SMS)

def test_cannot_decrease_max_supply_to_zero(mox, owner):
    with boa.env.prank(owner.address):
        with boa.reverts(mox.ERROR_NO_ZERO()):
            mox.decrease_max_supply(0)

def test_cannot_decrease_max_supply_to_current_max_supply(mox, owner):
    with boa.env.prank(owner.address):
        with boa.reverts(mox.ERROR_CAN_NOT()):
            mox.decrease_max_supply(SMS)

def test_non_owner_cannot_increase_max_supply(mox, non_owner):
    with boa.env.prank(non_owner):
        with boa.reverts(mox.ERROR_NOT_OWNER()):
            mox.increase_max_supply(IMS)
         

