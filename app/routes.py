import io
from flask import request, render_template, send_file

from app import app
from app.cipher import Playfair, SuperEnkripsi, Vigenere
from app.forms import PlayfairForm, SuperEnkripsiForm, VigenereForm


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    form = PlayfairForm()
    if request.method == 'POST':
        output = ""
        if form.validate_on_submit():
            cipher = Playfair(form.key.data)
            if form.encrypt.data:
                output = cipher.encrypt(form.input.data)
            elif form.decrypt.data:
                output = cipher.decrypt(form.input.data)
        return render_template('playfair.html', form=form, output=output)
    else:
        return render_template('playfair.html', form=form)


@app.route('/super-enkripsi', methods=['GET', 'POST'])
def super_enkripsi():
    form = SuperEnkripsiForm()
    if request.method == 'POST':
        output = ""
        if form.validate_on_submit():
            cipher = SuperEnkripsi(form.key.data)
            if form.encrypt.data:
                output = cipher.encrypt(form.input.data)
            elif form.decrypt.data:
                output = cipher.decrypt(form.input.data)
        return render_template('super-enkripsi.html', form=form, output=output)
    else:
        return render_template('super-enkripsi.html', form=form)


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    form = VigenereForm()
    if request.method == 'POST':
        output = ""
        if form.validate_on_submit():
            # Input processing
            input = ""
            if form.input_text.data:
                input = form.input_text.data
            elif form.input_file.has_file():
                input = ''.join(map(chr, form.input_file.data.read()))
            key = form.key.data
            matrix_mode = (Vigenere.MatrixMode.MATRIX_MODE_FULL if form.matrix_mode.data == 'matrix_full'
                           else Vigenere.MatrixMode.MATRIX_MODE_BASIC)
            seed = form.seed.data or '1337'
            key_mode = (Vigenere.KeyMode.KEY_MODE_AUTO if form.key_mode.data == 'key_auto'
                        else Vigenere.KeyMode.KEY_MODE_BASIC)
            char_size = (Vigenere.CharSize.CHAR_SIZE_EXTENDED if form.char_size.data == 'size_256'
                         else Vigenere.CharSize.CHAR_SIZE_BASIC)
            # Encryption process
            cipher = Vigenere(key, seed=seed, key_mode=key_mode, matrix_mode=matrix_mode, char_size=char_size)
            if form.encrypt.data:
                output = cipher.encrypt(input)
            elif form.decrypt.data:
                output = cipher.decrypt(input)
            # Return
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, output)))
        return render_template('vigenere.html', form=form, output=output)
    else:
        return render_template('vigenere.html', form=form)


def send_byte_as_file(bytes, outfile_name='data.out'):
    return send_file(io.BytesIO(bytes), as_attachment=True,
                     attachment_filename=outfile_name,
                     mimetype='application/octet-stream')
