"""
 A Module for Encrypt and Decrypt message
"""

import ReadWriteFileManagement
# Import the Fernet module
from cryptography.fernet import Fernet

DATABASE_DIR_PATH = "../../databases/chat_db/"
FILE_NAME = "encryptKey.key"

"""
A function for generating an encryption key.
the function generate the using Fernet class,
and saves the key into file in a specific path
"""


def generate_encryption_key():
    # generate a random key for encryption
    encrypt_key = Fernet.generate_key()
    # Writing the key into a file in order to decode the messages when needed
    if ReadWriteFileManagement.create_chat_file(FILE_NAME) is not None:
        ReadWriteFileManagement.create_chat_file(FILE_NAME)
    # Stores the encryption key into the encryption file
    with open(DATABASE_DIR_PATH + FILE_NAME, 'wb') as encryptKey:
        encryptKey.write(encrypt_key)


"""
A function for Encrypt a text message
"""


def message_encrypt(message_to_encrypt):
    # Opening the file that stores the encrypt key
    with open(DATABASE_DIR_PATH + FILE_NAME, 'rb') as en_Key:
        key = en_Key.read()
    # Creating an instant of the Fernet class with encrypt_key,
    # so we can encrypt each message using Fernet methods
    fernet = Fernet(key)

    # E ncrypt message
    enc_message = fernet.encrypt(message_to_encrypt.encode())
    return enc_message


"""
A function for Decrypt a text message
"""


def message_decrypt(message_to_decrypt):
    # Opening the file that stores the encrypt key
    with open(DATABASE_DIR_PATH + FILE_NAME, 'rb') as encryptKey:
        key = encryptKey.read()
    # Creating an instant of the Fernet class with encrypt_key,
    # so we can encrypt each message using Fernet methods
    fernet = Fernet(key)
    decode_message = fernet.decrypt(message_to_decrypt.decode())
    return decode_message


if __name__ == "__main__":
    generate_encryption_key()
    message = "Hello"
    enc_m = message_encrypt(message)
    print(enc_m.decode())
    dec_m = message_decrypt(enc_m)
    print(dec_m.decode())
