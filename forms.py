from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField,SelectField
#from wtforms.validators import 


class Library (FlaskForm):
    title = StringField (label='Book title')
    amount = IntegerField ('Amount')
    availble = BooleanField ('Availble')
    condition = SelectField ( 'good' , choices=[('good'),('bad'),('JakCieMoge')])