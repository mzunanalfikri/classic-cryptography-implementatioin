from app import app
from app.cipher.vigenere import Vigenere


@app.route('/', methods=['GET'])
def home():
    print('-------')
    cipher = Vigenere('TEST.*9A', key_mode=Vigenere.KeyMode.KEY_MODE_AUTO, matrix_mode=Vigenere.MatrixMode.MATRIX_MODE_FULL,
                      char_size=Vigenere.CharSize.CHAR_SIZE_EXTENDED)
    inp = 'ABCDEFGHI*(@)*#EWdlfalkdfj'
    print(inp)
    ct = cipher.encrypt(inp)
    print(ct)
    pt = cipher.decrypt(ct)
    print(pt)
    print('-------')
    assert inp == pt
    return 'Hello world!'
