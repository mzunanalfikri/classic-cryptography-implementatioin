import numpy as np
from sympy import Matrix

class Hill:
    def __init__(self, matrixKey):
        self.key = np.mod(np.array(matrixKey), 26)
        # check determinan first
        if (np.linalg.det(self.key) == 0):
            raise Exception("Matrix key invalid")
        self.inversKey = np.array(Matrix(self.key).inv_mod(26).tolist())

    def _generate_trigram(self, text):
        text = text.upper()
        if (len(text)%3 == 1):
            text = text + "XX"
        elif (len(text)%3 == 2):
            text = text + "X"

        trigram = []
        for i in range(0, len(text), 3):
            trigram.append(np.array([[ord(text[i]) % 65], [ord(text[i+1])%65], [ord(text[i+2])%65 ]]))
        return trigram

    def _dot_helper(self, text, matrix):
        trigram = self._generate_trigram(text)
        result = ""
        for el in trigram:
            temp = (np.mod(np.dot(matrix, el),26))
            result += chr(temp[0][0] + 65)
            result += chr(temp[1][0] + 65)
            result += chr(temp[2][0] + 65)
        return(result)

    def encrypt(self, plainText):
        plainText = ''.join(filter(str.isalpha, plainText.upper())) #filter alphanumeric only
        return(self._dot_helper(plainText, self.key))

    def decrypt(self, ciphetText):
        temp = (self._dot_helper(ciphetText, self.inversKey))
        #check padding
        if (temp[-2:] == "XX"):
            return (temp[:-2])
        elif (temp[-1:] == "X"):
            return (temp[:-1])

if __name__ == "__main__":
    # mat = [[17,17,5],[21,18,21],[2,2,19]]
    # mat = [[0,0,0],[21,18,21],[2,2,19]]
    obj = Hill(mat)
    print(obj.encrypt("paym oremo ne --++ yo"))
    print(obj.decrypt(obj.encrypt("paymoremoneyo")))