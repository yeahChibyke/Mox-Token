from moccasin.boa_tools import VyperContract 
from src import mox_token
from eth_utils import to_wei

MAX_SUPPLY = to_wei(1000, "ether")

def deploy() -> VyperContract:
    mox_contract: VyperContract = mox_token.deploy(MAX_SUPPLY)
    print(f"Mox token deployed to the following address: {mox_contract.address}")
    return mox_contract

def moccasin_main() -> VyperContract:
    deploy()

