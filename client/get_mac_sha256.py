import hashlib
import uuid

def get_sha256_mac():
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    hash_object = hashlib.sha256(mac_address.encode())
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

hash_result = get_sha256_mac()
print(f"Le hash SHA-256 de l'adresse MAC est : {hash_result}")