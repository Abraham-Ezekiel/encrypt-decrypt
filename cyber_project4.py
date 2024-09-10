#!/bin/python3

from cryptography.fernet import Fernet

# Load the key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt a file
def encrypt_file(file_path, cipher_suite):
    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)
    encrypted_file_path = file_path + ".encrypted"

    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{file_path}' has been encrypted and saved as '{encrypted_file_path}'")

# Function to decrypt a file
def decrypt_file(encrypted_file_path, cipher_suite):
    with open(encrypted_file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)
    decrypted_file_path = encrypted_file_path.replace(".encrypted", ".decrypted")

    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{encrypted_file_path}' has been decrypted and saved as '{decrypted_file_path}'")

# Main program
def main():
    # Load the encryption key
    key = load_key()
    cipher_suite = Fernet(key)

    action = input("Do you want to (e)ncrypt or (d)ecrypt a file? ").lower()

    if action == 'e':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, cipher_suite)
    elif action == 'd':
        encrypted_file_path = input("Enter the path of the file to decrypt: ")
        decrypt_file(encrypted_file_path, cipher_suite)
    else:
        print("Invalid action. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()

