from flask import Flask, render_template, url_for,request,redirect
from flask_wtf import FlaskForm
import json
from forms import Library
from models import Books

app = Flask (__name__)
app.config['SECRET_KEY'] = 'blabla'


@app.route ('/', methods = ['GET','POST'])
def index():
    form = Library()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():       #spr czy dane do form zostały poprawnie wpisane dane.
            Books.create(form.data)
            Books.save_all()
        return redirect(url_for("index"))
    """if form.validate_on_submit():
        return f'blabla'
    return render_template("index.html", form=form)"""
    

