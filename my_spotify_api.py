import tekore as tk
import spotify

client_id = 'f908f6f5d766436a8b0570af37c4bcbe'
client_secret = 'f140673ff7424cb599e24cbb8490446c'

def get_api_token():
    return tk.request_client_token(client_id, client_secret)
    
