import string 
def create_cipher_alphabet(keyword): 
    keyword = ''.join(sorted(set(keyword), key=keyword.index)) 
    remaining_letters = ''.join([ch for ch in string.ascii_lowercase if ch not in keyword]) 
    return keyword + remaining_letters 

def encrypt_monoalphabetic(plain_text, keyword): 
    cipher_alphabet = create_cipher_alphabet(keyword) 
    plain_alphabet = string.ascii_lowercase 
    encryption_table = str.maketrans(plain_alphabet, cipher_alphabet) 
    encrypted_text = plain_text.translate(encryption_table) 
    return encrypted_text 
def decrypt_monoalphabetic(encrypted_text, keyword): 
    cipher_alphabet = create_cipher_alphabet(keyword) 
    plain_alphabet = string.ascii_lowercase 
    decryption_table = str.maketrans(cipher_alphabet, plain_alphabet) 
    decrypted_text = encrypted_text.translate(decryption_table) 
    return decrypted_text 

# User input 
message = input("Enter the message: ").lower() 
keyword = input("Enter the keyword: ").lower() 
encrypted_message = encrypt_monoalphabetic(message, keyword) 
print("Encrypted:", encrypted_message) 
decrypted_message = decrypt_monoalphabetic(encrypted_message, keyword) 
print("Decrypted:", decrypted_message)
