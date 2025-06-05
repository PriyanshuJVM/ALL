def generate_key(text, key):
    key = key.upper()
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    key = generate_key(plain_text, key)
    cipher_text = ""
    for p, k in zip(plain_text, key):
        encrypted_char = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
        cipher_text += encrypted_char
    return cipher_text

def decrypt_vigenere(cipher_text, key):
    key = generate_key(cipher_text, key)
    orig_text = ""
    for c, k in zip(cipher_text, key):
        decrypted_char = chr(((ord(c) - ord(k) + 26) % 26) + ord('A'))
        orig_text += decrypted_char
    return orig_text

text = input("Enter the message: ").upper().replace(" ", "")
keyword = input("Enter the key: ").upper()

encrypted = encrypt_vigenere(text, keyword)
decrypted = decrypt_vigenere(encrypted, keyword)

print("\n Encrypted Message:", encrypted)
print(" Decrypted Message:", decrypted)
