import web3

from web3 import Web3
import solc

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.17;

contract Direction {
    enum DirectionChoices { Left, Right, Straight, Pause }
    DirectionChoices choice;
    DirectionChoices constant defaultChoice = DirectionChoices.Straight;

    function setLeft() public {
        choice = DirectionChoices.Left;
    }
    function setRight() public {
        choice = DirectionChoices.Right;
    }

    function getChoice() public view returns (DirectionChoices) {
        return choice;
    }

    function getDefaultChoice() public pure returns (uint) {
        return uint(defaultChoice);
    }
}
'''

compiled_sol = solc.compile_source(
    contract_source_code)  # Compiled source code
contract_interface = compiled_sol['<stdin>:Direction']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Instantiate and deploy contract
Direction = w3.eth.contract(
    abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Direction.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Create the contract instance with the newly-deployed address
direction = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'], )

# Display the default greeting from the contract
print('Contract Direction (before): {}'.format(direction.functions.getChoice()
                                               .call()))

print('Setting the direction...')
tx_hash = direction.functions.setRight().transact()

# Wait for transaction to be mined...
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the default greeting from the contract
print('Contract Direction (after): {}'.format(direction.functions.getChoice()
                                              .call()))
