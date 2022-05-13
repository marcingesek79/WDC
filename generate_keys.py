from Crypto.PublicKey import RSA

key = RSA.generate(2048)

# generating private key
private_key = key.export_key()
file_out = open("private_key.pem", "wb")
file_out.write(private_key)
file_out.close()

# generating public key
public_key = key.publickey().export_key()
file_out = open("public_key.pem", "wb")
file_out.write(public_key)
file_out.close()