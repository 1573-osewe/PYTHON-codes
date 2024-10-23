# Importing required libraries
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from base64 import urlsafe_b64encode, urlsafe_b64decode

# Function to derive a key from a password
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(password))

# Function to generate a new salt
def generate_salt():
    return os.urandom(16)

# Interactive usage
password_input = input("Enter your password: ").encode()  # Convert to bytes
salt_option = input("Would you like to provide a salt? (yes/no): ")

if salt_option.lower() == 'yes':
    salt_input = input("Enter your salt (in base64 format): ").encode()
    salt = urlsafe_b64decode(salt_input)  # Decode the base64 input
else:
    salt = generate_salt()  # Generate a random salt

# Derive the key
key = derive_key(password_input, salt)

print(f"Derived key: {key.decode()}")  # Decoded for readability
print(f"Salt (base64): {urlsafe_b64encode(salt).decode()}")
