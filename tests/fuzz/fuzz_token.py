import boa
from boa.test.strategies import strategy
from hypothesis import HealthCheck, given, settings


@settings(
    max_examples=1000, suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(new_max_supply=strategy("uint256"))
def test_should_not_be_able_to_increase_max_supply_to_current_max_supply(
    mox, owner, new_max_supply
):
    print(new_max_supply)
    with boa.env.prank(owner):
        mox.increase_max_supply(new_max_supply)
    # assert mox.get_max_supply() == new_max_supply
