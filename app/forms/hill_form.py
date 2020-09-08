from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class HillForm(FlaskForm):
    input = StringField('Input Text', widget=TextArea(), validators=[DataRequired()])
    mat = StringField('Matrix Key', widget=TextArea(), validators=[DataRequired()])
    output_as_file = BooleanField('Output as File')
    encrypt = SubmitField('Encrypt')
    decrypt = SubmitField('Decrypt')

    def generateMatrix(self):
        mat = (self.mat.data.split("\r\n"))
        count = 0
        for i in range(len(mat)):
            mat[i] = mat[i].split(" ")
            for j in range(len(mat[i])):
                mat[i][j] = int(mat[i][j])
                count = count + 1
        return mat