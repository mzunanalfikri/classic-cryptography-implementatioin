from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class SuperEnkripsiForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    key = StringField('Key', validators=[DataRequired()])
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')
