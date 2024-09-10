#!/bin/python3

from cryptography.fernet import Fernet

# Load the key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt text
def encrypt_text(plain_text, cipher_suite):
    encrypted_text = cipher_suite.encrypt(plain_text.encode())
    print(f"Encrypted: {encrypted_text}")
    return encrypted_text

# Function to decrypt text
def decrypt_text(encrypted_text, cipher_suite):
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    print(f"Decrypted: {decrypted_text}")
    return decrypted_text

# Main program
def main():
    # Load the encryption key
    key = load_key()
    cipher_suite = Fernet(key)

    action = input("Do you want to (e)ncrypt or (d)ecrypt text? ").lower()

    if action == 'e':
        plain_text = input("Enter the text to encrypt: ")
        encrypted_text = encrypt_text(plain_text, cipher_suite)
    elif action == 'd':
        encrypted_text_input = input("Enter the text to decrypt: ")
        encrypted_text = encrypted_text_input.encode()  # Convert input string to bytes
        decrypt_text(encrypted_text, cipher_suite)
    else:
        print("Invalid action. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()

