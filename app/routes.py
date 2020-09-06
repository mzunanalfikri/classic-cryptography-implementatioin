from flask import request, render_template

from app import app
from app.cipher import Playfair, Vigenere
from app.forms import PlayfairForm, VigenereForm


@app.route('/', methods=['GET'])
def home():
    return 'Hello World'


@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    form = PlayfairForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            cipher = Playfair(form.key.data)
            output = None
            if form.encrypt.data:
                output = cipher.encrypt(form.input.data)
            elif form.decrypt.data:
                output = cipher.decrypt(form.input.data)
        return render_template('playfair.html', form=form, output=output)
    else:
        return render_template('playfair.html', form=form)


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    form = VigenereForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            input = form.input.data
            key = form.key.data
            matrix_mode = (Vigenere.MatrixMode.MATRIX_MODE_FULL if form.matrix_mode.data == 'matrix_full'
                           else Vigenere.MatrixMode.MATRIX_MODE_BASIC)
            seed = form.seed.data
            key_mode = (Vigenere.KeyMode.KEY_MODE_AUTO if form.key_mode.data == 'key_auto'
                        else Vigenere.KeyMode.KEY_MODE_BASIC)
            char_size = (Vigenere.CharSize.CHAR_SIZE_EXTENDED if form.char_size.data == 'size_256'
                         else Vigenere.CharSize.CHAR_SIZE_BASIC)
            # Encryption process
            cipher = Vigenere(key, seed='1337', key_mode=key_mode, matrix_mode=matrix_mode, char_size=char_size)
            output = None
            if form.encrypt.data:
                output = cipher.encrypt(input)
            elif form.decrypt.data:
                output = cipher.decrypt(input)
        return render_template('vigenere.html', form=form, output=output)
    else:
        return render_template('vigenere.html', form=form)
