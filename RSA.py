from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt_decrypt():
    message = input("Enter message to encrypt with RSA: ").encode()

    key = RSA.generate(2048)
    public_key = key.publickey()
    private_key = key

    cipher_rsa_enc = PKCS1_OAEP.new(public_key)
    encrypted = cipher_rsa_enc.encrypt(message)
    print(f"Encrypted: {encrypted.hex()}")

    cipher_rsa_dec = PKCS1_OAEP.new(private_key)
    decrypted = cipher_rsa_dec.decrypt(encrypted)
    print(f"Decrypted: {decrypted.decode()}")

rsa_encrypt_decrypt()
