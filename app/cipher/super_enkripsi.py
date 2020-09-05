
class SuperEnkripsi:

    def __init__(self, key):
        self.vigenereKey = key
        temp = 0
        for _ in key:
            temp += ord(_)
        self.transposisiKey = temp % 3 + 2

    def encrypt(self, plainText):
        print(plainText)

    def decrypt(self, cipherText):
        print(cipherText)