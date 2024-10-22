def one_time_pad_encrypt(plaintext, key): 
    ciphertext = [] 
    for i in range(len(plaintext)): 
        # XOR operation to encrypt 
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i])) 
        ciphertext.append(encrypted_char) 
    return ''.join(ciphertext) 

def one_time_pad_decrypt(ciphertext, key): 
    decrypted_text = [] 
    for i in range(len(ciphertext)): 
        # XOR operation to decrypt 
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i])) 
        decrypted_text.append(decrypted_char) 
    return ''.join(decrypted_text) 

# Example usage: 
plaintext = "Hey Heet" 
key = "randomkey12345" # Note: Key length must be same as plaintext length for OTP 
# Encryption 
encrypted_text = one_time_pad_encrypt(plaintext, key) 
print("Encrypted:", encrypted_text) 
# Decryption 
decrypted_text = one_time_pad_decrypt(encrypted_text, key) 
print("Decrypted:", decrypted_text) 
