from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class SuperEnkripsiForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    key = StringField('Key', validators=[DataRequired()])
    output_as_file = BooleanField('Output as File')
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')
