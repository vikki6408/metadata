from web3 import Web3
import time
 
# === CONFIGURATION ===
RPC_URL = "http://10.229.43.182:8545"
PRIVATE_KEY = "3942de5719b6c29bbb621737eedc24dc32e2192e1390875baaafa1404112692a"
 
# Connexion à la blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))
print(f"Connected: {web3.is_connected()}")
 
# Obtenir l'adresse publique depuis la clé privée
account = web3.eth.account.from_key(PRIVATE_KEY)
sender_address = account.address
print(f"Expéditeur : {sender_address}")
 
# === Données intégrées : Liste des PDFs avec URL et hash SHA-256 ===
pdf_hashes = [
    {
        "url": "file:///N:/Commun/ELEVE/INFO/SI-MI2b/C107/Vikki.pdf",
        "sha256": "82fe33aae0b7841ce3c0280a4e4b8901e456c6046eb903bbf02432412665932c"
    }
]
 
# Nonce de départ
nonce = web3.eth.get_transaction_count(sender_address)
 
# Envoi de chaque hash
print("\n--- Envoi des hashes dans la blockchain ---")
for i, entry in enumerate(pdf_hashes):
    try:
        url = entry.get("url")
        sha256 = entry.get("sha256")
 
        if not sha256:
            print(f"[{i}] Hash manquant, entrée ignorée.")
            continue
 
        tx = {
            'nonce': nonce + i,
            'to': '0x0000000000000000000000000000000000000000',
            'value': 0,
            'gas': 50000,
            'gasPrice': web3.to_wei('1', 'gwei'),
            'chainId': web3.eth.chain_id,
            'data': web3.to_bytes(hexstr=sha256)
        }
 
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
 
        print(f"[{i}] Hash envoyé pour {url} ➜ TX: {web3.to_hex(tx_hash)}")
        time.sleep(0.3)
 
    except Exception as e:
        print(f"[{i}] Erreur pour {url} : {e}")