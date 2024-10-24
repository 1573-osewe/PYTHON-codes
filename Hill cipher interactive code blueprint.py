import numpy as np

# Function to calculate the modular inverse of a matrix
def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Find the determinant
    det_inv = pow(det, -1, modulus)  # Find modular inverse of the determinant
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_mod_inv

# Function to encrypt the message using the Hill Cipher
def hill_encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")  # Convert message to uppercase and remove spaces
    if len(message) % key_matrix.shape[0] != 0:
        # Pad the message with 'X' if it's not a multiple of matrix size
        message += 'X' * (key_matrix.shape[0] - len(message) % key_matrix.shape[0])

    message_vector = [ord(char) - ord('A') for char in message]  # Convert message to numeric values (0-25)
    message_vector = np.array(message_vector).reshape(-1, key_matrix.shape[0])
    
    encrypted_vector = (np.dot(message_vector, key_matrix) % 26).flatten()  # Matrix multiplication and mod 26
    encrypted_message = ''.join(chr(num + ord('A')) for num in encrypted_vector)  # Convert back to letters
    return encrypted_message

# Function to decrypt the message using the Hill Cipher
def hill_decrypt(encrypted_message, key_matrix):
    encrypted_message = encrypted_message.upper().replace(" ", "")  # Prepare encrypted message
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)  # Get the inverse of the key matrix

    encrypted_vector = [ord(char) - ord('A') for char in encrypted_message]
    encrypted_vector = np.array(encrypted_vector).reshape(-1, key_matrix.shape[0])
    
    decrypted_vector = (np.dot(encrypted_vector, key_matrix_inv) % 26).flatten()
    decrypted_message = ''.join(chr(num + ord('A')) for num in decrypted_vector)
    return decrypted_message

# Function to get the matrix from user input
def get_key_matrix(size):
    print(f"Enter the {size}x{size} key matrix (row-wise, space-separated):")
    matrix = []
    for i in range(size):
        row = input(f"Row {i+1}: ").strip().split()
        row = [int(num) for num in row]
        matrix.append(row)
    return np.array(matrix)

# Main function to run the interactive Hill cipher
def main():
    print("Welcome to the Hill Cipher!")
    
    action = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    while action not in ('e', 'd'):
        action = input("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt: ").lower()
    
    message = input("Enter the message: ").upper()
    
    # Get the matrix size and key matrix
    matrix_size = int(input("Enter the size of the key matrix (e.g., 2 for 2x2, 3 for 3x3): "))
    key_matrix = get_key_matrix(matrix_size)
    
    if action == 'e':
        encrypted_message = hill_encrypt(message, key_matrix)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = hill_decrypt(message, key_matrix)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
