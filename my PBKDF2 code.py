from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[len(text) - 1:])]

def encrypt(plaintext, password):
    salt = get_random_bytes(16)

    key = PBKDF2(password, salt, dkLen=32, count=1000000)

    cipher = AES.new(key,AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext).encode('utf-8'))
    return base64.b64encode(salt + cipher.iv + ciphertext).decode('utf-8')

def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext)
    salt = ciphertext[:16]
    iv = ciphertext[16:32]
    actual_ciphertext = ciphertext[32:]
    
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(actual_ciphertext).decode('utf-8'))
    return plaintext

if __name__ == "__main__":
    while True:
        print("AES Encryption & Decryption (Password-Based)")
        password = input("Enter a password to generate encryption key:")

        message = input("Enter a message to encrypt(or 'exit' to quit:) ")
        if message.lower() == 'exit':
            break

        encrypted_message = encrypt(message, password)
        print(f"Encrypted: {encrypted_message}")

        decrypt_choice = input("Do you want to decrypt this message? (yes/no):")
        if decrypt_choice.lower() == 'yes':
            decrypted_message = decrypt(encrypted_message, password)
            print(f"Decrypted: {decrypted_message}")

        print("-" * 40)
        
        
