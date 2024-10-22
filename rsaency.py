import random 
from sympy import mod_inverse, isprime 

def generate_prime(bits=8): 
    while True: 
        prime_candidate = random.getrandbits(bits) 
        if isprime(prime_candidate): 
            return prime_candidate 
        
def mod_exp(base, exponent, modulus): 
    return pow(base, exponent, modulus) 

def generate_rsa_keys(): 
    # Step 1: Select two prime numbers (p and q) 
    p = generate_prime(bits=8) 
    q = generate_prime(bits=8) 
    n  = p * q 
    # Step 2: Compute Euler's totient function phi(n) 
    phi_n = (p - 1) * (q - 1) 
    # Step 3: Choose public exponent e such that 1 < e < phi(n) and e is coprime with phi(n) 
    e = 65537 
    # Step 4: Compute the private key d (modular inverse of e mod phi(n)) 
    d = mod_inverse(e, phi_n) 
    return (n, e), (n, d) 

# RSA Encryption 
def rsa_encrypt(plaintext, public_key): 
    n, e = public_key 
    # Convert plaintext characters to integers, then encrypt each integer 
    ciphertext = [mod_exp(ord(char), e, n) for char in plaintext] 
    return ciphertext 

# RSA Decryption 
def rsa_decrypt(ciphertext, private_key): 
    n, d = private_key
    # Decrypt each integer, then convert it back to characters 
    decrypted_text = ''.join([chr(mod_exp(char, d, n)) for char in ciphertext]) 
    return decrypted_text 



# Example usage of RSA 
public_key, private_key = generate_rsa_keys() 
print(f"Public Key: {public_key}") 
print(f"Private Key: {private_key}") 
# Original message 
message = "HEET" 
print(f"\nOriginal message: {message}") 
# Encryption 
encrypted_message = rsa_encrypt(message, public_key) 
print(f"Encrypted message: {encrypted_message}") 
# Decryption 
decrypted_message = rsa_decrypt(encrypted_message, private_key) 
print(f"Decrypted message: {decrypted_message}") 