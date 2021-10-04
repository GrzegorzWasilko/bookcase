from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField,SelectField
from wtforms.validators import DataRequired,required
#from wtforms.validators import 


class Library (FlaskForm):
    title = StringField (label='Book title')
    id = IntegerField (label='id',validators=[DataRequired()])
    availble = BooleanField ('Availble')
    condition = SelectField ( 'good' , choices=[('good'),('bad condition'),('JakCieMoge')])

#Mylibrary =[{}]
class id (FlaskForm):
    ID=IntegerField (label='ID',validators=[DataRequired()])