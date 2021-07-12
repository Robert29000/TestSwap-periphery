import os
from brownie import TestSwapRouter, accounts

def main():
    test_account = accounts.add(os.getenv("PRIVATE_KEY"))
    wbnb_address_test = '0xAaE79b63555C3e77Eb5011d78F21DaE16F5c4Ed1';
    factory_address_test = '0x5359aD30170bCf38BE1A7E5C8CE8e2AC1ED2BeaE';
    token = TestSwapRouter.deploy(factory_address_test, wbnb_address_test, {'from': test_account})