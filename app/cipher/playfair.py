import math
import string


class Playfair:

    def __init__(self, key):
        self.key = key.upper().replace(" ", "")
        self.asciiToIndexMap = self._generate_matrix(False)
        self.indexToAsciiMap = self._generate_matrix(True)

    def _generate_matrix(self, isIndexToAscii):
        matrix = []
        ASCII_EXCEPT_J = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for _ in self.key:
            if ((_ not in matrix) and (_ != "J")) :
                matrix.append(_)
        
        for _ in ASCII_EXCEPT_J:
            if _ not in matrix:
                matrix.append(_)     
        
        matrix_map = {}
        for i in range(len(matrix)):
            matrix_map[matrix[i]] = (i//5, i%5)

        if (isIndexToAscii):
            matrix_map = dict(map(reversed, matrix_map.items()))

        return matrix_map

    def _generate_bigram(self, plainTeks):
        array_pt = list(plainTeks.upper().replace(" ", "").replace("J", "I"))

        #insert X if 2 string same
        for i in range(len(array_pt)-1):
            if (array_pt[i] == array_pt[i+1]):
                array_pt.insert(i+1, "X")

        #insert X if len string is odd
        if (len(array_pt) % 2 == 1):
            array_pt.append("X")
        
        bigram = []
        for i in range(0, len(array_pt), 2):
            bigram.append([array_pt[i], array_pt[i+1]])

        return bigram

    def encrypt(self, plainTeks):
        bigram = self._generate_bigram(plainTeks)
        print(bigram)
        result = []
        for el in bigram:
            p1 = self.asciiToIndexMap[el[0]]
            p2 = self.asciiToIndexMap[el[1]]
            if (p1[0] == p2[0]): #sekolom
                result.append(self.indexToAsciiMap[(p1[0],(p1[1]+1)%5)])
                result.append(self.indexToAsciiMap[(p2[0],(p2[1]+1)%5)])
            elif (p1[1] == p2[1]): # sebaris
                result.append(self.indexToAsciiMap[((p1[0]+1)%5,p1[1])])
                result.append(self.indexToAsciiMap[((p2[0]+1)%5,p2[1])])
            else:
                result.append(self.indexToAsciiMap[(p1[0],p2[1])])
                result.append(self.indexToAsciiMap[(p2[0],p1[1])])
        return("".join(result))
    
    def decrypt(self, cipherTeks):
        if (len(cipherTeks) % 2 == 1):
            raise Exception("Cipher text invalid.")
        
        result = []
        bigram = []
        for i in range(0, len(cipherTeks), 2):
            bigram.append([cipherTeks[i].upper(), cipherTeks[i+1].upper()])

        for el in bigram:
            p1 = self.asciiToIndexMap[el[0]]
            p2 = self.asciiToIndexMap[el[1]]
            if (p1[0] == p2[0]): #sekolom
                result.append(self.indexToAsciiMap[(p1[0],(p1[1]-1)%5)])
                result.append(self.indexToAsciiMap[(p2[0],(p2[1]-1)%5)])
            elif (p1[1] == p2[1]): # sebaris
                result.append(self.indexToAsciiMap[((p1[0]-1)%5,p1[1])])
                result.append(self.indexToAsciiMap[((p2[0]-1)%5,p2[1])])
            else:
                result.append(self.indexToAsciiMap[(p1[0],p2[1])])
                result.append(self.indexToAsciiMap[(p2[0],p1[1])])
        return("".join(result))

#untuk test
if __name__ == "__main__":
    obj = Playfair("JALAN GANESHA SEPULUH")
    obj.decrypt(obj.encrypt("temui ibu nanti malam"))
    