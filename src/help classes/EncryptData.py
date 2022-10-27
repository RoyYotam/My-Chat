from hashlib import sha256
# importing the Fernet module
from cryptography.fernet import Fernet


# A Class for encrypt a password using hash function
# using hash library -> SHA256

class HashPassword(object):
    # Construct an instant of the PassWord encryption using SHA256.
    # Assigning an instant of the SHA256 class, that transforms a random-size input into a fixed-size bit string.
    # returns a hexDecimal rep of a password with fixed length - 64.
    def __init__(self, password):
        self.h_instant = sha256()
        self.h_instant.update(bytes(password, 'utf-8'))
        self.hash = ''
        self.hash_password()

    # Hashing the password by converting the bytes' rep of h_instant into hex decimal rep
    def hash_password(self):
        self.hash = self.h_instant.hexdigest()

    def __str__(self):
        return self.hash


if __name__ == "__main__":
    code = HashPassword(input())
    print(code)

"""
A Class for encrypt chat - files using cryptography lab using fernet class.
"""


class EncryptFile(object):
    ENCRYPTION_KEY = Fernet.generate_key()
    with open('encryptKey.key', 'wb') as encryptKey:
        encryptKey.write(ENCRYPTION_KEY)
    def __init__(self, file_name):
        # generating the encryption's key
        self.encrypt_file(file_name)

    """
    A method for encrypt the the designated file
    """

    def encrypt_file(self, file_name):
        # Opening the file that stores the encrypt key
        with open('encryptKey.key', 'rb') as encryptKey:
            key = encryptKey.read()
        # Creating an instant of the Fernet object for using the key
        fernet = Fernet(key)
        # Opening the original file for read and storing it into a variable
        with open(file_name, 'rb') as file:
            original_file = file.read()
        # Encrypt the Original file in a file_encrypt
        file_to_encrypt = Fernet.encrypt(original_file)
        # Writing the encrypted data in the original file (file_name)
        with open(file_name, 'wb') as encrypted_file:
            encrypted_file.write(file_to_encrypt)

    def file_decrypt(self, file_name):
        # Opening the file that stores the encrypt key
        with open('encryptKey.key', 'rb') as encryptKey:
            key = encryptKey.read()
        # Creating an instant of the Fernet object for using the key
        fernet = Fernet(key)

        # Opening the encrypted file
        with open(file_name, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        # Decrypt the file and store it into an object
        decrypted = Fernet.decrypt(encrypted)
        # Writing the decrypted data in the original file (file_name)
        with open(file_name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)


if __name__ == "__main__":
    file_name = "ma.txt"
    encrypt = EncryptFile(file_name)