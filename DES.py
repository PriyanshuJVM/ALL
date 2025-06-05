from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt_decrypt():
    key = input("Enter 8-byte DES key: ").encode()
    if len(key) != 8:
        print("DES key must be exactly 8 bytes.")
        return

    data = input("Enter message to encrypt: ").encode()
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, DES.block_size))
    print(f"Encrypted: {ct_bytes.hex()}")

    cipher_dec = DES.new(key, DES.MODE_CBC, iv=cipher.iv)
    pt = unpad(cipher_dec.decrypt(ct_bytes), DES.block_size)
    print(f"Decrypted: {pt.decode()}")

des_encrypt_decrypt()
