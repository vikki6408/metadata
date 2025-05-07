from web3 import Web3
 
# Connexion au nœud Ethereum
w3 = Web3(Web3.HTTPProvider('http://10.229.43.182:8545/'))
if not w3.is_connected():
    print("Erreur de connexion à la blockchain.")
    exit()
 
# Obtenir le nombre total de blocs
block_count = w3.eth.block_number
 
# Parcourir les blocs
for i in range(1, block_count + 1):
    try:
        block = w3.eth.get_block(i, full_transactions=True)
        print(f"\nBloc {i} :")
        print(f"Hash : {block.hash.hex()}")
        print(f"Nombre de transactions : {len(block.transactions)}")
 
        # Parcourir les transactions du bloc
        for tx in block.transactions:
            print(f"\nTransaction Hash : {tx.hash.hex()}")
            print(f"De : {tx['from'] if 'from' in tx else 'N/A'}")
            print(f"À : {tx['to'] if 'to' in tx else 'N/A'}")
            print(f"Valeur : {w3.from_wei(tx['value'], 'ether')} ETH")
            print(f"Gas utilisé : {tx['gas']}")
            print(f"Prix du Gas : {w3.from_wei(tx['gasPrice'], 'gwei')} Gwei")
    except Exception as e:
        print(f"Erreur lors de la récupération du bloc {i} : {e}")