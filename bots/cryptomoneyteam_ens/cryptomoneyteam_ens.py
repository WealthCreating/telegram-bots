import telegram
from web3.auto.infura import w3

from ens.auto import ns

# confirm the connection was successful
w3.isConnect()

# Look up the address of an ENS domain
eth_address = ns.address('cryptomoneyteam.eth')

# Subdomains
ns.setup_addresss('test.cryptomoneyteam.eth', address='point to this hex address'))

# Connect address
web3.personal.importRawKey(private_key, 'password')

# Unlock address
web3.personal.unlockAccount(address, 'password')
