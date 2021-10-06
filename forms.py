from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField,SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired,required
#from wtforms.validators import 


class Library (FlaskForm):
    title = StringField (label='Book title',validators=[DataRequired()])
    id = IntegerField (label='id',validators=[DataRequired()])
    availble = BooleanField ('Availble',validators=[DataRequired()])
    condition = SelectField ( 'good' , choices=[('good'),('bad condition'),('JakCieMoge')])
    submit= SubmitField ('Add new position')
