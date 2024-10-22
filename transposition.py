def encrypt_message(message, key): 
    # Create an empty list with 'key' number of strings 
    ciphertext = [''] * key 
    # Loop through each column in the key 
    for col in range(key): 
        pointer = col 
        # Add characters to the column until the end of the message 
        while pointer < len(message): 
            ciphertext[col] += message[pointer] 
            pointer += key 
    # Join the list of strings to form the encrypted message 
    return ''.join(ciphertext) 

def decrypt_message(ciphertext, key): 
    # Calculate the number of columns, rows, and shaded boxes 
    num_columns = (len(ciphertext) + key - 1) // key # Round up to handle any remaining characters 
    num_rows = key 
    num_shaded_boxes = (num_columns * key) - len(ciphertext) 
    # Create a list of empty strings for the plaintext message 
    plaintext = [''] * num_columns 
    col = 0 
    row = 0 
    # Loop through each character in the ciphertext 
    for symbol in ciphertext: 
        plaintext[col] += symbol 
        col += 1 
        # If we've reached the last column or encountered a shaded box, reset the column and move to the next row 
        if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_shaded_boxes): 
            col = 0 
            row += 1
    # Join the list of strings to form the decrypted message 
    return ''.join(plaintext) 

# Input from the user 
message = input("Enter the message to be encrypted: ") 
key = int(input("Enter the key (number of columns for encryption): ")) 
# Encrypt the message 
encrypted_message = encrypt_message(message, key) 
print("Encrypted:", encrypted_message) 
# Decrypt the message 
decrypted_message = decrypt_message(encrypted_message, key) 
print("Decrypted:", decrypted_message)
