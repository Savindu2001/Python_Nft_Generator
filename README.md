# PNFT Generator
This is a simple Python script for generating NFTs using the OpenZeppelin library.

# Requirements
Python 3.7 or higher
web3 library (pip install web3)
openzeppelin-contracts library (pip install openzeppelin-contracts)

# Usage
Update the private_key variable in the script with the private key of the account that will be used to sign the transactions.
Update the nft_contract_abi.json and nft_contract_bytecode.json files with the compiled ABI and bytecode of the NFT contract that you want to deploy.
Run the script with python nft_generator.py.
The script will deploy the NFT contract and mint a new NFT with token ID 1 and a specified token URI.

# Example
Here's an example of how to use the script:

csharp
Copy code
$ python nft_generator.py
NFT created with token ID 1 and owner: 0x1234567890abcdef1234567890abcdef12345678

# Comments
This code was written by Savindu Senanayake.
