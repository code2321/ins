def generate_vigenere_table(): 
    table = [] 
    for i in range(26): 
        row = [(chr(((i + j) % 26) + 65)) for j in range(26)] 
        table.append(row) 
    return table 

def encrypt_vigenere(plain_text, keyword): 
    table = generate_vigenere_table() 
    keyword_repeated = (keyword * (len(plain_text) // len(keyword))) + keyword[:len(plain_text) % len(keyword)] 
    plain_text = plain_text.upper().replace(" ", "") 
    keyword_repeated = keyword_repeated.upper() 
    encrypted_text = "" 
    for p, k in zip(plain_text, keyword_repeated): 
        if p.isalpha(): 
            row = ord(k) - 65 
            col = ord(p) - 65 
            encrypted_text += table[row][col] 
        else: 
            encrypted_text += p 
    return encrypted_text 

def decrypt_vigenere(encrypted_text, keyword): 
    table = generate_vigenere_table() 
    keyword_repeated = (keyword * (len(encrypted_text) // len(keyword))) + keyword[:len(encrypted_text) % len(keyword)] 
    encrypted_text = encrypted_text.upper().replace(" ", "") 
    keyword_repeated = keyword_repeated.upper() 
    decrypted_text = "" 
    for c, k in zip(encrypted_text, keyword_repeated): 
        if c.isalpha(): 
            row = ord(k) - 65 
            col = table[row].index(c) 
            decrypted_text += chr(col + 65) 
        else: 
            decrypted_text += c 
    return decrypted_text


# User input 
message = input("Enter the message: ") 
keyword = input("Enter the keyword: ") 
encrypted_message = encrypt_vigenere(message, keyword) 
print("Encrypted:", encrypted_message) 
decrypted_message = decrypt_vigenere(encrypted_message, keyword) 
print("Decrypted:", decrypted_message)