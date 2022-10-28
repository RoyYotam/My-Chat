from hashlib import sha256


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

if __name__ == "__main__":
    pass