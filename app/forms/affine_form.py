from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class AffineForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    m = IntegerField('M Key (relative prime with 26)', validators=[DataRequired("Integer Required.")])
    b = IntegerField('B key', validators=[DataRequired("Integer Required.")])
    # m = StringField('')
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')