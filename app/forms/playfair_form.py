from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class PlayfairForm(FlaskForm):
    input_text = StringField('Input Text', widget=TextArea())
    input_file = FileField('Input File')
    key = StringField('Key', validators=[DataRequired()])
    output_as_file = BooleanField('Output as File')
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
