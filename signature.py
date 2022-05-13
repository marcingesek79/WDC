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
    file = open(signature_file, "wb")
    file.write(signature)
    file.close()


"""
    Function that verifies digital signature.

    INPUT:
    - key - sender's public key
    - data - signature data
    - signature_file - file that contains signature

    OUTPUT:
    returns 'true' if signature is verified correctly
    otherwise returns 'false'

"""

def verify_signature(key, data, signature_file):
    hash = SHA256.new(data)
    sender_public_key = RSA.import_key(key)
    signer = PKCS1_v1_5.new(sender_public_key)
    file = open(signature_file, "rb")
    signature = file.read()
    
    if (signer.verify(hash, signature)):
        return True
    else:
        return False
