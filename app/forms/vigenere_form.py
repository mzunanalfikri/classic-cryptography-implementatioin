from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class VigenereForm(FlaskForm):
    input_text = StringField('Input Text', widget=TextArea())
    input_file = FileField('Input File')
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
    char_size = RadioField('Char Size', choices=[
        ('size_26', '26x26'),
        ('size_256', '256x256 (Extended Vigenere)'),
    ])
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        # Custom validation
        if self.input_text.data and self.input_file.has_file():
            self.input_text.errors.append('Please use one of input_text or input_file, not both')
            self.input_file.errors.append('Please use one of input_text or input_file, not both')
            return False
        if (not self.input_text.data) and (not self.input_file.has_file()):
            self.input_text.errors.append('No input specified')
            self.input_file.errors.append('No input specified')
            return False
        return True
