def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    
    if choice not in ('E', 'D'):
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
        return
    
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = encrypt_caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt_caesar_cipher(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
