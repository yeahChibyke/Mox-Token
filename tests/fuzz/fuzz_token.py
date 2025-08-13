import boa
from boa.test.strategies import strategy
from hypothesis import settings
from hypothesis.stateful import RuleBasedStateMachine, rule

from src import mox_token


class MaxSupplyIncreaseAndDecreaseFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = mox_token.deploy()
        print("Contract deployed!!!")

    @rule(new_max_supply = strategy("uint256"))
    def increase_max_supply(self, new_max_supply):
        with boa.env.prank(self.contract.owner):
            self.contract.increase_max_supply(new_max_supply)
            response = self.contract.get_max_supply()
            assert response == new_max_supply, f"Expected {new_max_supply}, got {response}"
            print(f"called increase_max_supply with {new_max_supply}")

    @rule(new_max_supply = strategy("uint256"))
    def decrease_max_supply(self, new_max_supply):
        with boa.env.prank(self.contract.owner):
            self.contract.decrease_max_supply(new_max_supply)
            response = self.contract.get_max_supply()
            assert response == new_max_supply, f"Expected {new_max_supply}, got {response}"
            print(f"Called decrease_max-supply with {new_max_supply}")

TokenFuzzing = MaxSupplyIncreaseAndDecreaseFuzzer.TestCase
TokenFuzzing.settings = settings(max_examples=1000, stateful_step_count=50)

