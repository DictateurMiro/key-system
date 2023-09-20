from flask import Flask, request, jsonify
import json

app = Flask(__name__)

try:
    with open("key.json", "r") as f:
        key_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    key_data = {}  
    
@app.route('/', methods=['POST'])
def verify_key():
    client_key = request.json.get('key', '')

    if client_key in key_data:
        return jsonify({'response': key_data[client_key]})
    else:
        return jsonify({'response': 'non'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
