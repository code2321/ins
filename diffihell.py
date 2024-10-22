import random


def mod_exp(base, exponent, modulus): 
    return pow(base, exponent, modulus) 
def diffie_hellman(): 
    # Step 1: Agree on a prime number (p) and a base (g) publicly 
    p = 23 # A small prime number for simplicity (in practice, use a large prime) 
    g = 5 # A primitive root modulo p (in practice, use a large base) 
    print(f"Publicly shared variables:\nPrime (p): {p}, Base (g): {g}") 
    # Step 2: Alice and Bob choose their private keys (secret numbers) 
    alice_private_key = random.randint(1, p-1) 
    bob_private_key = random.randint(1, p-1) 
    print(f"\nAlice's private key: {alice_private_key}") 
    print(f"Bob's private key: {bob_private_key}") 
    # Step 3: Alice and Bob compute their public keys 
    alice_public_key = mod_exp(g, alice_private_key, p) 
    bob_public_key = mod_exp(g, bob_private_key, p) 
    print(f"\nAlice's public key: {alice_public_key}") 
    print(f"Bob's public key: {bob_public_key}") 
    # Step 4: Exchange public keys over a public channel 
    # Step 5: Both compute the shared secret key 
    # Alice computes: (Bob's public key ^ Alice's private key) % p 
    alice_shared_secret = mod_exp(bob_public_key, alice_private_key, p) 
    # Bob computes: (Alice's public key ^ Bob's private key) % p 
    bob_shared_secret = mod_exp(alice_public_key, bob_private_key, p) 
    print(f"\nAlice's shared secret key: {alice_shared_secret}") 
    print(f"Bob's shared secret key: {bob_shared_secret}") 
    # The shared secret keys should be the same 
    assert alice_shared_secret == bob_shared_secret, "Error: Shared secrets do not match!" 
    print("\nShared secret key successfully established!") 

diffie_hellman()
