import string


class Enigma:
    # source: https://en.wikipedia.org/wiki/Enigma_rotor_details
    # rotor and reflector position:
    # | REFLECTOR | ROTOR_I | ROTOR_II | ROTOR_II |
    # encrypt - decrypt path:
    #   / ROTOR_I <- ROTOR_II <- ROTOR_III <- INPUT
    # REFLECTOR
    #   \ ROTOR_I -> ROTOR_II -> ROTOR_III -> OUTPUT
    # P.S.: plugboard not implemented for simplicity
    CHARSET = string.ascii_uppercase
    ROTOR_I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'  # using rotor I
    ROTOR_II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'  # using rotor II
    ROTOR_III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'  # using rotor III
    REFLECTOR = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'  # using reflector UKW-B

    def __init__(self, key_1, key_2, key_3):
        self.ROTOR_OFFSET_I = self.CHARSET.index(key_1[:1].upper())
        self.ROTOR_OFFSET_II = self.CHARSET.index(key_2[:1].upper())
        self.ROTOR_OFFSET_III = self.CHARSET.index(key_3[:1].upper())
        self.__init_enigma_shift_helper()

    def __init_enigma_shift_helper(self):
        # ord(output) - ord(input) value caused by each rotor and reflector (mod 26)
        # rotor_shift is ord shift caused by rotor when input is from right to left
        # rotor_shift for input from left to right need to be corrected relative to the input
        #     (see encryption process on ROTOR_I->ROTOR_II->ROTOR_III below)
        self.ROTOR_SHIFT_I = [(ord(self.ROTOR_I[i]) - ord(self.CHARSET[i])) % 26 for i in range(26)]
        self.ROTOR_SHIFT_II = [(ord(self.ROTOR_II[i]) - ord(self.CHARSET[i])) % 26 for i in range(26)]
        self.ROTOR_SHIFT_III = [(ord(self.ROTOR_III[i]) - ord(self.CHARSET[i])) % 26 for i in range(26)]
        self.REFLECTOR_SHIFT = [(ord(self.REFLECTOR[i]) - ord(self.CHARSET[i])) % 26 for i in range(26)]

    def encrypt(self, pt):
        # Encryption path: ROTOR_III->ROTOR_II->ROTOR_I->REFLECTOR->ROTOR_I->ROTOR_II->ROTOR_III
        ct = ''
        for cp in pt:
            imm_idx = self.CHARSET.index(cp)
            self.rotate()
            # ROTOR_III->ROTOR_II->ROTOR_I
            imm_idx = (imm_idx + self.ROTOR_SHIFT_III[(imm_idx + self.ROTOR_OFFSET_III) % 26]) % 26
            imm_idx = (imm_idx + self.ROTOR_SHIFT_II[(imm_idx + self.ROTOR_OFFSET_II) % 26]) % 26
            imm_idx = (imm_idx + self.ROTOR_SHIFT_I[(imm_idx + self.ROTOR_OFFSET_I) % 26]) % 26
            # REFLECTOR
            imm_idx = (imm_idx + self.REFLECTOR_SHIFT[(imm_idx) % 26]) % 26
            # ROTOR_I->ROTOR_II->ROTOR_III
            l_inp_idx = (imm_idx + self.ROTOR_OFFSET_I) % 26
            imm_pair_idx = self.ROTOR_I.index(self.CHARSET[l_inp_idx])
            imm_idx = (imm_idx - self.ROTOR_SHIFT_I[imm_pair_idx]) % 26
            l_inp_idx = (imm_idx + self.ROTOR_OFFSET_II) % 26
            imm_pair_idx = self.ROTOR_II.index(self.CHARSET[l_inp_idx])
            imm_idx = (imm_idx - self.ROTOR_SHIFT_II[imm_pair_idx]) % 26
            l_inp_idx = (imm_idx + self.ROTOR_OFFSET_III) % 26
            imm_pair_idx = self.ROTOR_III.index(self.CHARSET[l_inp_idx])
            imm_idx = (imm_idx - self.ROTOR_SHIFT_III[imm_pair_idx]) % 26
            print(self.CHARSET[imm_idx])
            # add new cp
            ct += self.CHARSET[imm_idx]
        return ct

    def decrypt(self, ct):
        # The encryption == decryption because it is one-to-one mapping between pt-ct
        return self.encrypt(ct)

    def rotate(self):
        # Simplified enigma rotate (all notch in Z)
        # Shift 1 from rightmost rotor (ROTOR_III)
        self.ROTOR_OFFSET_III = (self.ROTOR_OFFSET_III + 1) % 26
        if self.ROTOR_OFFSET_III != 0: return
        # If new self.ROTOR_OFFSET_III == 0, shift ROTOR_II
        self.ROTOR_OFFSET_II = (self.ROTOR_OFFSET_II + 1) % 26
        if self.ROTOR_OFFSET_II != 0: return
        # If new self.ROTOR_OFFSET_II == 0, shift ROTOR_I
        self.ROTOR_OFFSET_I = (self.ROTOR_OFFSET_I + 1) % 26


if __name__ == "__main__":
    inp = 'TESTGAN'
    out = Enigma('X', 'Z', 'W').encrypt(inp)
    new_inp = Enigma('X', 'Z', 'W').decrypt(out)
    print(inp)
    print(out)
    print(new_inp)
    assert inp == new_inp
