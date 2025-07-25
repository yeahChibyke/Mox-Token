# -- Imports -- #
import pytest 
from moccasin.config import get_active_network
from script.deploy import deploy, MAX_SUPPLY
# from eth_utils import to_wei
import boa 

# -- Session Fixtures -- #

@pytest.fixture(scope = "session")
def owner():
    return get_active_network().get_default_account()

@pytest.fixture(scope = "session")
def mox():
    return deploy()


# -- Function Fixtures -- #

@pytest.fixture(scope = "function")
def non_owner():
    return boa.env.generate_address("non_owner")

