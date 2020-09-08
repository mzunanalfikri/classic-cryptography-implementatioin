from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class AffineForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    m = IntegerField('M Key (relative prime with 26)', validators=[DataRequired("Integer Required.")])
    b = IntegerField('B key', validators=[DataRequired("Integer Required.")])
    output_as_file = BooleanField('Output as File')
    # m = StringField('')
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')