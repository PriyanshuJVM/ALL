# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# def aes_encrypt_decrypt():
#     key = input("Enter AES key (16, 24, or 32 bytes): ").encode()
#     if len(key) not in [16, 24, 32]:
#         print("Key must be 16, 24, or 32 bytes.")
#         return

#     data = input("Enter message to encrypt: ").encode()
#     cipher = AES.new(key, AES.MODE_CBC)
#     ct_bytes = cipher.encrypt(pad(data, AES.block_size))
#     print(f"Encrypted: {ct_bytes.hex()}")

#     cipher_dec = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
#     pt = unpad(cipher_dec.decrypt(ct_bytes), AES.block_size)
#     print(f"Decrypted: {pt.decode()}")

# aes_encrypt_decrypt()



from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_default_encrypt_decrypt():
    key = b'1234567890abcdef'  # 16 bytes
    #key_24 = b'thisis24bytekeystring!!!!'  # Exactly 24 bytes
    #key_32 = b'thisisaverysecure32bytekeystring!!'  # Exactly 32 bytes

    message = b'This is a secret message.'

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))

    print(f"Encrypted (hex): {cipher.iv.hex()}{ciphertext.hex()}")

    # Decryption
    cipher_dec = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
    plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

    print(f"Decrypted: {plaintext.decode()}")

aes_default_encrypt_decrypt()
