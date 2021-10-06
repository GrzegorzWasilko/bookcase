from flask import Flask, render_template, url_for,request,redirect
from flask_wtf import FlaskForm
import json
from forms import Library
from models import BooksForm

app = Flask (__name__)
app.config['SECRET_KEY'] = 'blabla'

books=BooksForm()                              #instancja  Books z pliku json

@app.route ('/', methods = ['GET','POST'])
def index():
    form = Library()                        #tworzy sie klasa formularza
    if request.method == "POST":            #sprawdza czy walidacje (metody) sie powiodły 
        if form.validate_on_submit():       #spr czy dane do form zostały poprawnie wpisane .
            books.create(form.data)         # dopisuje do objektu.klasyBooks dane z formularza
            books.save_all()               # zapisuje stan pliku json 
        return redirect(url_for('index')) #wracam do index

    return render_template('index.html', form=form, books=books.all())# get powoduje wyswietlenie form i listy z books
#________________________________________________________________________________________________________________
@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update(id):
    book = books.get(id - 1)
    form = BooksForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(id - 1, form.data)
        return redirect(url_for("index"))
    return render_template("update.html", form=form, books=book, id=id)