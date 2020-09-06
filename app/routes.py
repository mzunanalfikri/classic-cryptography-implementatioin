from app import app
from app.cipher.vigenere import Vigenere


@app.route('/', methods=['GET'])
def home():
    return 'Hello world!'
