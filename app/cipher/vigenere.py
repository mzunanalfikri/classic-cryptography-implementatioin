import math
import string
import random
import re
from enum import Enum


class Vigenere(object):
    """Vigenere cipher class"""

    # KeyMode enum
    class KeyMode(Enum):
        KEY_MODE_BASIC = 0
        KEY_MODE_AUTO = 1

    # MatrixMode enum
    class MatrixMode(Enum):
        MATRIX_MODE_BASIC = 0
        MATRIX_MODE_FULL = 1

    # CharSize enum
    class CharSize(Enum):
        CHAR_SIZE_BASIC = 26
        CHAR_SIZE_EXTENDED = 256

    def __init__(self, key, seed='1337', key_mode=KeyMode.KEY_MODE_BASIC,
                 matrix_mode=MatrixMode.MATRIX_MODE_BASIC,
                 char_size=CharSize.CHAR_SIZE_BASIC):
        # Check params
        if not isinstance(key_mode, self.KeyMode):
            raise TypeError('key_mode must be KeyMode, not ' + type(key_mode).__name__)
        if not isinstance(matrix_mode, self.MatrixMode):
            raise TypeError('matrix_mode must be MatrixMode, not ' + type(matrix_mode).__name__)
        if not isinstance(char_size, self.CharSize):
            raise TypeError('char_size must be CharSize, not ' + type(char_size).__name__)
        # Assign properties
        self.key = key
        self.seed = seed
        self.key_mode = key_mode
        self.matrix_mode = matrix_mode
        self.char_size = char_size
        # Filter key if use char basic
        if self.char_size == self.CharSize.CHAR_SIZE_BASIC:
            self.key = re.sub(r'[^A-Za-z]', '', self.key).upper()
        # Generate matrix for encryption and decryption
        self.__generate_matrix()

    def __generate_matrix(self):
        # Get raw char list for each matrix row
        if self.char_size == self.CharSize.CHAR_SIZE_BASIC:
            raw_char_list = list(string.ascii_uppercase)
        else:  # self.CharSize.CHAR_SIZE_EXTENDED
            raw_char_list = [chr(i) for i in range(256)]
        # Scramble matrix row based on self.matrix_mode
        if self.matrix_mode == self.MatrixMode.MATRIX_MODE_BASIC:
            rows = [dict(zip(raw_char_list, raw_char_list[i:] + raw_char_list[:i]))
                    for i in range(self.char_size.value)]
        else:  # self.MatrixMode.MATRIX_MODE_FULL
            random.seed(self.seed)
            rows = [dict(zip(raw_char_list, random.sample(raw_char_list, self.char_size.value)))
                    for i in range(self.char_size.value)]
        self.matrix = dict(zip(raw_char_list, rows))

    def encrypt(self, pt):
        # Filter char if not extended vigenere
        if self.char_size == self.CharSize.CHAR_SIZE_BASIC:
            pt = re.sub(r'[^A-Za-z]', '', pt).upper()
        # Generate encryption key
        if self.key_mode == self.KeyMode.KEY_MODE_BASIC:
            key = (self.key * math.ceil(len(pt) / len(self.key)))[:len(pt)]
        else:  # self.KeyMode.KEY_MODE_AUTO
            key = (self.key + pt)[:len(pt)]
        # Encrypt
        ct = ''
        for cp, ck in zip(pt, key):
            ct += self.matrix[ck][cp]
        return ct

    def __decrypt_helper(self, ck, cc):
        for k, v in self.matrix[ck].items():
            if v == cc: return k
        return None

    def decrypt(self, ct):
        # Filter char if not extended vigenere
        if self.char_size == self.CharSize.CHAR_SIZE_BASIC:
            ct = re.sub(r'[^A-Za-z]', '', ct).upper()
        # Get initial decryption key
        if self.key_mode == self.KeyMode.KEY_MODE_BASIC:
            key = (self.key * math.ceil(len(ct) / len(self.key)))[:len(ct)]
        else:  # self.KeyMode.KEY_MODE_AUTO
            key = self.key
        # Decrypt
        pt = ''
        counter = 0
        while counter < len(ct):
            cc, ck = ct[counter], key[counter]
            temp = self.__decrypt_helper(ck, cc)
            if temp:
                pt += temp
            else:
                raise Exception('Cannot map ciphertext to plaintext')
            counter += 1
            # Update key if key_mode == KEY_MODE_AUTO
            if self.key_mode == self.KeyMode.KEY_MODE_AUTO:
                key += pt[-1]
        return pt


if __name__ == '__main__':
    cipher = Vigenere('TEST.*9A', key_mode=Vigenere.KeyMode.KEY_MODE_AUTO, matrix_mode=Vigenere.MatrixMode.MATRIX_MODE_FULL,
                      char_size=Vigenere.CharSize.CHAR_SIZE_EXTENDED)
    inp = 'ABCDEFGHI*(@)*#EWdlfalkdfj'
    print(inp)
    ct = cipher.encrypt(inp)
    print(ct)
    pt = cipher.decrypt(ct)
    print(pt)
    assert inp == pt
