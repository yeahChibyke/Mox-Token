# ------------------------------------------------------------------
#                             IMPORTS
# ------------------------------------------------------------------


# from eth_utils import to_wei
import boa
import pytest

# from moccasin.config import get_active_network
from script.deploy import deploy

# ------------------------------------------------------------------
#                         SESSION FIXTURES
# ------------------------------------------------------------------


@pytest.fixture(scope="session")
def owner(mox):
    # return get_active_network().get_default_account()
    return mox.owner()


@pytest.fixture(scope="session")
def mox():
    return deploy()


@pytest.fixture(scope="session")
def mx_sup(mox):
    return mox.get_max_supply()


# ------------------------------------------------------------------
#                        FUNCTION FIXTURES
# ------------------------------------------------------------------


@pytest.fixture(scope="function")
def non_owner():
    return boa.env.generate_address("non_owner")
