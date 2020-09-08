from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class HillForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    mat = StringField('Matrix Key', widget=TextArea(), validators=[DataRequired()])
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')

    def generateMatrix(self):
        print(self.mat.data)
        return [[1,3,4],[4,5,6],[7,8,9]]