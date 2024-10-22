import numpy as np 

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")

def create_key_matrix(key, size):
    key_matrix = [] 
    for i in range(size): 
        row = [ord(char) - 65 for char in key[i*size:(i+1)*size]] 
        key_matrix.append(row) 
    return np.array(key_matrix)

def encrypt_hill(plain_text, key, size): 
    key_matrix = create_key_matrix(key, size) 
    plain_text = plain_text.upper().replace(" ", "") 
 
    while len(plain_text) % size != 0: 
        plain_text += 'X' 
    cipher_text = "" 
    for i in range(0, len(plain_text), size): 
        block = [ord(char) - 65 for char in plain_text[i:i+size]] 
        block_vector = np.array(block).reshape(size, 1) 
        encrypted_vector = np.dot(key_matrix, block_vector) % 26 
        cipher_text += ''.join(chr(int(num) + 65) for num in encrypted_vector) 
 
    return cipher_text 

def decrypt_hill(cipher_text, key, size): 
    key_matrix = create_key_matrix(key, size) 
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26 
    inverse_determinant = mod_inverse(determinant, 26) 

    # Calculate the adjugate matrix 
    adjugate_matrix = np.zeros((size, size), dtype=int) 
    for i in range(size): 
        for j in range(size): 
            # Get minor matrix 
            minor = np.delete(np.delete(key_matrix, i, axis=0), j, axis=1) 
            adjugate_matrix[j][i] = ((-1) ** (i + j)) * int(np.round(np.linalg.det(minor))) % 26
    adjugate_matrix = (inverse_determinant * adjugate_matrix) % 26

    plain_text = "" 
    for i in range(0, len(cipher_text), size): 
        block = [ord(char) - 65 for char in cipher_text[i:i+size]] 
        block_vector = np.array(block).reshape(size, 1) 
        decrypted_vector = np.dot(adjugate_matrix, block_vector) % 26 
        plain_text += ''.join(chr(int(num) + 65) for num in decrypted_vector) 
    
    return plain_text

# User input 
message = input("Enter the message: ") 
key = input("Enter the 4-letter key: ") 
size = 2 
encrypted_message = encrypt_hill(message, key, size) 
print("Encrypted:", encrypted_message) 
decrypted_message = decrypt_hill(encrypted_message, key, size) 
print("Decrypted:", decrypted_message) 

 
