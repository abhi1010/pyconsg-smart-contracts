import web3

from web3 import Web3
from solc import compile_source
import pprint
import time


def compile_source_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()

    return compile_source(source)


def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).deploy()

    address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    return address


def wait_for_receipt(w3, tx_hash, poll_interval):
    while True:
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        if tx_receipt:
            return tx_receipt
        time.sleep(poll_interval)


w3 = Web3(Web3.EthereumTesterProvider())

contract_source_path = 'storevar.sol'
compiled_sol = compile_source_file(contract_source_path)

contract_id, contract_interface = compiled_sol.popitem()

print('contract_interface:abi={}'.format(contract_interface['abi']))
print('contract_interface:bin={}'.format(contract_interface['bin']))

address = deploy_contract(w3, contract_interface)
print("Deployed {0} to: {1}\n".format(contract_id, address))

store_var_contract = w3.eth.contract(
    address=address, abi=contract_interface['abi'])

gas_estimate = store_var_contract.functions.setVar(255).estimateGas()
print("Gas estimate to transact with setVar: {0}\n".format(gas_estimate))

if gas_estimate < 100000:
    print("Sending transaction to setVar(255)\n")
    tx_hash = store_var_contract.functions.setVar(255).transact()
    receipt = wait_for_receipt(w3, tx_hash, 1)
    print("Transaction receipt mined: \n")
    pprint.pprint(dict(receipt))
else:
    print("Gas cost exceeds 100000")
