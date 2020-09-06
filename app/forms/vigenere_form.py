from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired


class VigenereForm(FlaskForm):
    input = StringField('Input Text', validators=[DataRequired()])
    key = StringField('Key', validators=[DataRequired()])
    matrix_mode = RadioField('Matrix Mode', choices=[
        ('matrix_basic', 'Shift (Basic Vigenere)'),
        ('matrix_full', 'Shuffle (Full Vigenere)'),
    ])
    seed = StringField('Random Matrix Seed (Only used in Full Vigenere. Keep it blank to use server default value (seed=1337).)')
    key_mode = RadioField('Key Mode', choices=[
        ('key_basic', 'Basic Key'),
        ('key_auto', 'Auto Key (Auto-Key Vigenere)'),
    ])
    matrix_size = RadioField('Matrix Size', choices=[
        ('size_26', '26x26'),
        ('size_256', '256x256 (Extended Vigenere)'),
    ])
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')
