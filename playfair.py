#prac 3 : Implement Playfair cipher encryption-decryption

import itertools

def create_matrix(key):
    key = ''.join(sorted(set(key), key=key.index)).replace('j', 'i')
    # Create the 5x5 matrix
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = ''.join([c for c in key if c in alphabet] + [c for c in alphabet if c not in key])
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(char, matrix):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def process_digraphs(message):
    message = message.replace('j', 'i')
    digraphs = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
        else:
            b = 'x'
        if a == b:
            digraphs.append(a + 'x')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    if len(digraphs[-1]) == 1:
        digraphs[-1] += 'x'
    return digraphs

def encrypt_digraph(digraph, matrix):
    a_row, a_col = find_position(digraph[0], matrix)
    b_row, b_col = find_position(digraph[1], matrix)
    if a_row == b_row:
        return matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        return matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
    else:
        return matrix[a_row][b_col] + matrix[b_row][a_col]

def decrypt_digraph(digraph, matrix):
    a_row, a_col = find_position(digraph[0], matrix)
    b_row, b_col = find_position(digraph[1], matrix)
    if a_row == b_row:
        return matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
    elif a_col == b_col:
        return matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
    else:
        return matrix[a_row][b_col] + matrix[b_row][a_col]

def encrypt_playfair(message, key):
    matrix = create_matrix(key)
    digraphs = process_digraphs(message)
    encrypted_message = ''.join([encrypt_digraph(digraph, matrix) for digraph in digraphs])
    return encrypted_message

def decrypt_playfair(encrypted_message, key):
    matrix = create_matrix(key)
    digraphs = process_digraphs(encrypted_message)
    decrypted_message = ''.join([decrypt_digraph(digraph, matrix) for digraph in digraphs])
    return decrypted_message

# User input
message = input("Enter the message (letters only): ").replace(" ", "").lower()
key = input("Enter the keyword: ").replace(" ", "").lower()
encrypted_message = encrypt_playfair(message, key)
print("Encrypted:", encrypted_message)
decrypted_message = decrypt_playfair(encrypted_message, key)
print("Decrypted:", decrypted_message)
