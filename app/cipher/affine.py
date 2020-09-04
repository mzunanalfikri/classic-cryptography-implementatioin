

class Affine:
    def __init__(self, m, b):
        relative_prime = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        if (m not in relative_prime):
            raise Exception("m invalid.")
        self.m = m #bilangan bulat yang relatif dengan 26
        self.b = b%26 #pergeseran
    
    def encrypt(self, plainText):
        plainText = ''.join(filter(str.isalpha, plainText.upper())) #filter alphanumeric only
        result = []
        for alphabet in plainText:
            result.append(chr((self.m * (ord(alphabet)%65) + self.b)%26+65))
        return("".join(result))

    def decrypt(self, cipherText):
        cipherText = cipherText.upper()
        result = []
        for alphabet in cipherText:
            result.append(chr(self.modInverse26(self.m)*(ord(alphabet)%65 - self.b) % 26 + 65))
        print("".join(result))

    def modInverse26(self, a) : 
        m = 26
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

#test
if __name__ == "__main__":
    obj = Affine(7, 10)
    print(obj.encrypt("kriptoo"))
    obj.decrypt(obj.encrypt("kripto"))