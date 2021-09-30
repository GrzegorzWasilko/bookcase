from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField,SelectField
#from wtforms.validators import 


class Library (FlaskForm):
    title = StringField (label='Book title')
    id = IntegerField ('id')
    availble = BooleanField ('Availble')
    condition = SelectField ( 'good' , choices=[('good'),('bad condition'),('JakCieMoge')])

Mylibrary =[{}]
