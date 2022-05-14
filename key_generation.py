from Crypto.PublicKey import RSA

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
    if format != ".pem" and format != ".der" and format != ".key":
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
