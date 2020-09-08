import io
from flask import request, render_template, send_file

from app import app
from app.cipher import Playfair, SuperEnkripsi, Vigenere, Affine, Hill
from app.forms import PlayfairForm, SuperEnkripsiForm, VigenereForm, AffineForm, HillForm


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/affine', methods=['GET', 'POST'])
def affine():
    form = AffineForm()
    if request.method == 'POST':
        output = ""
        not_prime = False
        if form.validate_on_submit():
            try:
                cipher = Affine(form.m.data,form.b.data)
                if form.encrypt.data:
                    output = cipher.encrypt(form.input.data)
                elif form.decrypt.data:
                    output = cipher.decrypt(form.input.data)
            except :
                not_prime = True
                return render_template('affine.html', form=form, not_prime = not_prime)
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, output)), outfile_name='vigenere.txt')
        return render_template('affine.html', form=form, output = output)
    else:
        return render_template('affine.html', form=form)

@app.route('/hill', methods=['GET', 'POST'])
def hill():
    form = HillForm()
    if request.method == 'POST':
        output = ""
        isMatrixInvalid = False
        if form.validate_on_submit():
            try:
                cipher = Hill(form.generateMatrix())
                if form.encrypt.data:
                    output = cipher.encrypt(form.input.data)
                elif form.decrypt.data:
                    output = cipher.decrypt(form.input.data)
            except :
                isMatrixInvalid = True
                return render_template('hill.html', form=form, isMatrixInvalid = isMatrixInvalid)
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, output)), outfile_name='hill.txt')
        return render_template('hill.html', form=form, output = output)
    else:
        return render_template('hill.html', form=form)

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
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, output)), outfile_name='playfair.txt')
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
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, output)), outfile_name='super-enkripsi.txt')
        return render_template('super-enkripsi.html', form=form, output=output)
    else:
        return render_template('super-enkripsi.html', form=form)


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    form = VigenereForm()
    if request.method == 'POST':
        ct = ""
        if form.validate_on_submit():
            # Input processing
            pt = ""
            if form.input_text.data:
                pt = form.input_text.data
            elif form.input_file.has_file():
                pt = ''.join(map(chr, form.input_file.data.read()))
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
                ct = cipher.encrypt(pt)
            elif form.decrypt.data:
                ct = cipher.decrypt(pt)
            # Return
            if form.output_as_file.data:
                return send_byte_as_file(bytes(map(ord, ct)), outfile_name='vigenere.txt')
        return render_template('vigenere.html', form=form, output=ct)
    else:
        return render_template('vigenere.html', form=form)


def send_byte_as_file(data_bytes, outfile_name='data.out'):
    return send_file(io.BytesIO(data_bytes), as_attachment=True,
                     attachment_filename=outfile_name,
                     mimetype='application/octet-stream')
