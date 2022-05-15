from Crypto.PublicKey import RSA
import os

FORMATS = [
    ".der",
    ".pem",
    ".key"
]

"""
    Function that generates public and private key pair.

    INPUT:
    - format - ".pem" / ".key" / ".der"
    - private_key_name - name of private key file OPTIONAL
    - public_key_name - name of public key file OPTIONAL

    OUTPUT:
    creating file with public key and file with private key

"""

# generating private and public key pair
def generate_key_pair(format, private_key_name = "private_key", public_key_name = "public_key"):
    if format not in FORMATS:
        print("Wrong format")
        return

    key = RSA.generate(2048)
    
    # generating private key
    private_key = key.export_key()
    file_out = open(private_key_name + format, "wb")
    file_out.write(private_key)
    file_out.close()

    # generating public key
    public_key = key.publickey().export_key()
    file_out = open(public_key_name + format, "wb")
    file_out.write(public_key)
    file_out.close()


"""
    Function that removes all generated keys with .pem, .der, .key extensions.

    INPUT:
    - path - dir the files will be removed from
             if path is not passed, then the keys will be removed from current (app) dir

    OUTPUT:
    deleting key files
"""

def delete_keys(path = "."):
    dirs = os.listdir(path)
    for item in dirs:
        for format in FORMATS:
            if item.endswith(format):
                os.remove(os.path.join(path, item))
                break

