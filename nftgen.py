from web3 import Web3
from openzeppelin_contracts import OpenZeppelinContracts
from pathlib import Path
import json

# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))

# Set the private key of the account that will be used to sign the transactions
private_key = 'your-private-key'

# Load the OpenZeppelin contracts
openzeppelin_contracts = OpenZeppelinContracts(web3)

# Load the NFT contract ABI
nft_contract_abi_path = Path('nft_contract_abi.json')
with nft_contract_abi_path.open() as f:
    nft_contract_abi = json.load(f)

# Load the NFT contract bytecode
nft_contract_bytecode_path = Path('nft_contract_bytecode.json')
with nft_contract_bytecode_path.open() as f:
    nft_contract_bytecode = json.load(f)

# Deploy the NFT contract
nft_contract_factory = web3.eth.contract(abi=nft_contract_abi, bytecode=nft_contract_bytecode)
nft_contract_tx_hash = nft_contract_factory.constructor().transact({'from': web3.eth.accounts[0]})
nft_contract_address = web3.eth.waitForTransactionReceipt(nft_contract_tx_hash).contractAddress

# Create an NFT
nft_contract = web3.eth.contract(address=nft_contract_address, abi=nft_contract_abi)
token_uri = 'https://your-website.com/nft/1'
nft_contract.functions.mint(token_uri).transact({'from': web3.eth.accounts[0], 'gas': 500000})

# Get the owner of the NFT
nft_owner = nft_contract.functions.ownerOf(1).call()

print('NFT created with token ID 1 and owner:', nft_owner)
