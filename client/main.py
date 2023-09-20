import requests
import configparser
import hashlib
import uuid

def get_sha256_mac():
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    hash_object = hashlib.sha256(mac_address.encode())
    return hash_object.hexdigest()

def read_key_from_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT'].get('key', '')

key = read_key_from_config()
local_mac_hash = get_sha256_mac()

response = requests.post("http://adresse-ip:8080", json={"key": key})

if response.status_code == 200:
    server_response = response.json().get('response', 'non')
    if server_response == "non":
        print("La clé n'est pas valide.")
    else:
        server_mac_hash = server_response
        if server_mac_hash == local_mac_hash:
            #SUITE DE VOTRE PROGRAMME UNE FOIS QUE LA CLÉ FONCTIONNE
            print("Salut")
        else:
            print("La clé ne correspond pas à cette machine.")
else:
    print("Erreur lors de la connexion au serveur.")

