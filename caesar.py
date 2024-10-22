def encrypt_caesar(plain_text, shift): 
    encrypted_text = "" 
    for char in plain_text: 
        if char.isalpha(): 
            shift_amount = shift % 26 
            offset = 65 if char.isupper() else 97 
            encrypted_char = chr(((ord(char) - offset + shift_amount) % 26) + offset) 
            encrypted_text += encrypted_char 
        else: 
            encrypted_text += char 
    return encrypted_text 
def decrypt_caesar(encrypted_text, shift): 
    decrypted_text = "" 
    for char in encrypted_text: 
        if char.isalpha(): 
            shift_amount = shift % 26 
            offset = 65 if char.isupper() else 97 
            decrypted_char = chr(((ord(char) - offset - shift_amount) % 26) + offset) 
            decrypted_text += decrypted_char 
        else: 
            decrypted_text += char 
    return decrypted_text 
message = input("Enter the message: ") 
shift = int(input("Enter the shift value: ")) 
encrypted_message = encrypt_caesar(message, shift) 
print("Encrypted:", encrypted_message) 
decrypted_message = decrypt_caesar(encrypted_message, shift) 
print("Decrypted:", decrypted_message) 
