import random
# function to find the gcd

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a
#function to find the modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
        
        return None

#function to check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
        return True
# function to generate rsa keys
def generate_rsa_keys():
    # select two prime numbers
    p = int(input("P is not a prime. Enter a prime number P:"))
    q = int(input("Enter a prime number q:"))
    while not is_prime(q):
        q = int(input("q is not a prime. Enter a prime number q:"))
    # compute n and phi(n)
    n = p*q
    phi = (p-1) * (q-1) 
    #choose 'e' such that 1<e<phi(n) and gcd(e, phi(n))=1
    e = random.randrange(2, phi)
    while gcd(e, phi) !=1:
        e = random.randrange(2, phi)

    # compute the private key such that (e*d) % phi(n)=1
    d = mod_inverse(e, phi)
    print(f"Public key(e, n):({e},{n})")
    print(f"Private key(d, n):({d},{n})")

    return (e, n),(d, n)

# function to encrypt a message
def encrypt_rsa(message, public_key):
    e,n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]

    return encrypted_message
# function to decrypt the message
def decrypt_rsa(encrypted_message, private_key):
    d,n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])

    return decrypted_message

# main function to demonstrate RSA
def main ():
    print("RSA Encryption / Decryption")
    # generate keys
    public_key, private_key = generate_rsa_keys()
    # input the message
    message = input("Enter message to encrypt:")
    # encrypt the message
    encrypted_message = encrypt_rsa(message, public_key)
    print(f"Encrypted message:{encrypted_message}")

    # decrypt the message
    decrypted_message = decrypt_rsa(encrypted_message, private_key)
    print(f"Decrypted message:{decrypted_message}")

    if __name__ == "__main__" :
        main()
        
