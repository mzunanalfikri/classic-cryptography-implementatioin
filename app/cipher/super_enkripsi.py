from . import vigenere 
class SuperEnkripsi:

    def __init__(self, key):
        self.vigenereKey = key
        temp = 0
        for _ in key:
            temp += ord(_)
        self.transKey = temp % 3 + 2 #kemungkinan key 2,3,4
        self.vigenereCipher = vigenere.Vigenere(self.vigenereKey)

    def encrypt(self, plainText):
        plainText2 = self.vigenereCipher.encrypt(plainText)
        plainText2 = ''.join(filter(str.isalpha, plainText2.upper())) #filter alphanumeric only
        #padding
        plainText2 = plainText2 + ("_"*((self.transKey - (len(plainText2) % self.transKey))%self.transKey) )
        #make matrix
        matrix = ["" for i in range(self.transKey)]
        for i in range(len(plainText2)):
            j = i % self.transKey
            matrix[j] = matrix[j] + plainText2[i]

        return("".join(matrix))

    def decrypt(self, cipherText):
        matrix = ["" for i in range(len(cipherText)//self.transKey)]
        for i in range(len(cipherText)):
            j = i % (len(cipherText) // self.transKey)
            matrix[j] = matrix[j] + cipherText[i]

        result = self.vigenereCipher.decrypt("".join(matrix).replace("_", ""))
        return(result)


if __name__ == "__main__":
    obj = SuperEnkripsi("hehe")
    teks = obj.encrypt("a")
    print(teks)
    print(obj.decrypt(teks))
