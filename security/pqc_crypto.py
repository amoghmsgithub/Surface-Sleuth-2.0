from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_keys():
    key = get_random_bytes(32)
    return key, key  # symmetric for now

def encrypt_data(key, data: bytes):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext

def decrypt_data(key, nonce, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext)