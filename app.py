from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
import json
from forms import Library


app = Flask (__name__)
app.config['SECRET_KEY'] = 'blabla'


@app.route ('/', methods = ['GET','POST'])
def index():
    form = Library()

    if form.validate_on_submit():#spr czy dane do form zostały poprawnie wpisane dane.
        return f'''<ul>
                <li>{form.title.label} : {form.title.data}</li>
                <li>{form.amount.label} : {form.amount.data}</li>
                <li>{form.availble.label} : {form.availble.data}</li>
                <li>{form.condition.label} : {form.condition.data}</li>
                </ul>'''
    return render_template("index.html", form=form)
    

