from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# this function pads plaintext to be multiple block sizes
def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) %16)

# function to unpad plaintext after decryption
def unpad(text):
    return text[:-ord(text[len(text)- 1:])]

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext).encode('utf-8'))
    return base64.b64encode(cipher.iv + ciphertext).decode('utf-8')

def decrypt(ciphertext, key):
    ciphertext = base64.b64encode(ciphertext)
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]).decode('utf-8'))
    return plaintext

# main function ( interactive )
if __name__ == "__main__":

    key = get_random_bytes(16)

while True:
    message = input("Enter a message to encrypt(or 'exit' to quit):")
    if message.lower() =='exit':
        break

    #encrypt the message
    encrypted_message = encrypt(message, key)
    print(f"Encrypted: {encrypted_message}")

    #ask if user wants to decrypt
    decrypt_choice = input(" Do you want to decrypt this message? (yes/no):")
    if decrypt_choice.lower() == 'yes' :

        decrypted_message = decrypt(encrypted_message, key)
        print(f"Decrypted: {decrypted_message}")
    print("-" * 40)
    

