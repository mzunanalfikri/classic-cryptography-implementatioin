from flask import render_template

from app import app
from app.cipher import Vigenere
from app.forms import VigenereForm


@app.route('/', methods=['GET'])
def home():
    return 'Hello World'


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    form = VigenereForm()
    return render_template('vigenere.html', form=form)
