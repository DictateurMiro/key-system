import json
import random
import string

def generate_key_v2():
    possible_characters = string.ascii_uppercase + string.digits
    key = '-'.join([''.join(random.choices(possible_characters, k=5)) for _ in range(4)])
    
    return key

def add_key_to_json(mac_hash):
    new_key = generate_key_v2()

    try:
        with open("key.json", "r") as f:
            key_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        key_data = {}
        
    key_data[new_key] = mac_hash

    with open("key.json", "w") as f:
        json.dump(key_data, f)

    print(f"Clé {new_key} ajoutée et associée à l'adresse MAC hashée {mac_hash}.")

user_input = input("Veuillez entrer l'adresse MAC hashée: ")
add_key_to_json(user_input)
