from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# ----------- Diffie-Hellman Key Exchange ----------- #
def power_mod(base, exp, mod):
    return pow(base, exp, mod)

print("🔐 Diffie-Hellman Key Exchange")
#public parameters
q = int(input("Enter shared prime q: "))
p = int(input("Enter primitive root p: "))
#private keys
a = int(input("Enter A's private key: "))
b = int(input("Enter B's private key: "))

# Public keys
Y_A = power_mod(p, a, q)
Y_B = power_mod(p, b, q)

# Shared secret  keys
K_A = power_mod(Y_B, a, q)
K_B = power_mod(Y_A, b, q)

print(f"A's public value (Y_A): {Y_A}")
print(f"B's public value (Y_B): {Y_B}")
print(f"Shared secret key computed by A: {K_A}")
print(f"Shared secret key computed by B: {K_B}")

# ----------- Digital Signature Verification ----------- #
print("\n✍️ Digital Signature Verification")
message = input("Enter message to sign: ").encode()

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()


hash_msg = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(hash_msg)


hash_received = SHA256.new(message)
try:
    pkcs1_15.new(public_key).verify(hash_received, signature)
    print("Signature is valid. Message is from A and not tampered.")
except (ValueError, TypeError):
    print("Signature is invalid. Message may be tampered.")
