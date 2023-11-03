from sympy import randprime, Mod
from math import gcd

# Function to calculate multiplicative inverse
def multiplicative_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = extended_gcd(b % a, a)
            return g, y - (b // a) * x, x

    _, x, _ = extended_gcd(e, phi)
    return x % phi

# Function to encrypt using public key
def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

# Function to decrypt using private key
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)
p = randprime(2**5, 2**6)
q = randprime(2**5, 2**6)

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that it is coprime with phi
e = 2
while gcd(phi, e) != 1:
    e += 1

# Calculate multiplicative inverse of e under modulo phi
d = multiplicative_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)
print(f"Public key:{public_key}\nPrivate key:{private_key}")
plaintext = input("Input String:")
ciphertext = encrypt(public_key, plaintext)
decrypted_text = decrypt(private_key, ciphertext)

print("Original Text:", plaintext)
print("Encrypted Text:", ''.join(map(lambda x: chr(x), ciphertext)))
print("Decrypted Text:", decrypted_text)
