from web3 import Web3
import json

httpsUrl = "https://sepolia.infura.io/v3/76be8adc2030422a8b6c848bb83386f7"
w3 = Web3(Web3.HTTPProvider(httpsUrl))
print(w3.is_connected())

print(w3.eth.block_number)

address = "0x0e5DD0C6a40f524aa1faa51757Bf33A33262aA8d"
abi = json.loads(open('abi.json').read())
contract = w3.eth.contract(address=address, abi=abi)
pool = contract.functions

totSupply = pool.totalSupply().call()

print("total Supply:", totSupply)

events = contract.events.Choice.get_logs(fromBlock=472000)

print("event:", events[0])