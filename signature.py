from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

"""
    Function that generates digital signature.

    INPUT:
    - key - sender's private key path
    - data - signature data path
    - signature_file - file path that contains signature

    OUTPUT:
    changing the content of signature_file

"""

def generate_signature(key, data, signature_file="signature.pem"):
        hash = SHA256.new(open(data, "rb").read())
        try:
            sender_private_key = RSA.import_key(open(key).read())
            signature = PKCS1_v1_5.new(sender_private_key).sign(hash)
        except:
            print("This is not a private key")
            return
        
        file = open(signature_file, "wb")
        file.write(signature)
        file.close()


"""
    Function that verifies digital signature.

    INPUT:
    - key - sender's public key path
    - data - signature data path
    - signature_file - file path that contains signature

    OUTPUT:
    returns 'true' if signature is verified correctly
    otherwise returns 'false'

"""

def verify_signature(key, data, signature_file="signature.pem"):
    hash = SHA256.new(open(data, "rb").read())
    sender_public_key = RSA.import_key(open(key).read())
    signer = PKCS1_v1_5.new(sender_public_key)
    try:
        file = open(signature_file, "rb")
        signature = file.read()
        if (signer.verify(hash, signature)):
            return True
        else:
            return False
    except:
        print("Signature not found")
        return False

