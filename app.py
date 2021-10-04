from flask import Flask, render_template, url_for,request,redirect
from flask_wtf import FlaskForm
import json
from forms import Library
from models import books

app = Flask (__name__)
app.config['SECRET_KEY'] = 'blabla'


 
@app.route ('/', methods = ['GET','POST'])
def index():
    form = Library()
    error = "Cos tu nie idzie jak trzeba "
    if request.method == "POST":
        if form.validate_on_submit():       #spr czy dane do form zostały poprawnie wpisane .
            books.create(form.data)
            books.save_all()
            xxx = books.get(2)
            form = Library(data=books,xxx=xxx)#co tu sie dzieje
            
        return redirect(url_for('index',xxx=xxx))
    return render_template('index.html', form=form, books=books, error=error)

    """if form.validate_on_submit():
        return f'blabla'
    return render_template("index.html", form=form)"""
  #  form = Library(data=books)

