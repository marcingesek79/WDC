from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

"""
    Function that generates digital signature.

    INPUT:
    - key - sender's private key
    - data - signature data
    - signature_file - file that contains signature

    OUTPUT:
    changing the content of signature_file

"""

def generate_signature(key, data, signature_file):
    hash = SHA256.new(data)
    sender_private_key = RSA.import_key(key)
    signature = PKCS1_v1_5.new(sender_private_key).sign(hash)
    with open(signature_file, "wb") as f: f.write(signature)
    