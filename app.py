from flask import Flask, render_template, url_for,request,redirect
from flask_wtf import FlaskForm
import json
from forms import Library
from models import Books

app = Flask (__name__)
app.config['SECRET_KEY'] = 'blabla'

books=Books()                              #instancja  Books z pliku json

@app.route ('/', methods = ['GET','POST'])
def index():
    form = Library()                        #tworzy sie klasa formularza
    error = "Cos tu nie idzie jak trzeba  "
    if request.method == "POST":            #sprawdza czy walidacje (metody) sie powiodły 
        if form.validate_on_submit():       #spr czy dane do form zostały poprawnie wpisane .
            books.create(form.data)         # dopisuje do objektu.klasyBooks dane z formularza
            books.save_all()               # zapisuje stan pliku json 
        return redirect(url_for('index')) #wracam do index

    return render_template('index.html', form=form, books=books.all(), error=error)# get powoduje wyswietlenie form i listy z books
#________________________________________________________________________________________________________________
#@app.route ("/update")
#def update():                   
#    return render_template('update.html')

@app.route ("/update/<int:books_id>", methods = ['GET','POST']) #czyli n 1 element jest pod http://127.0.0.1:5000/index/2
def update(books_id):
    position = books.get(books_id - 1) # do position wpisuje dane z listy o indeksie w id o 1 mniejszym
    form = Library(data=position) # przekazuje do formularza Liblary dane z position 

    if request.method == "POST":
        if form.validate_on_submit():
           books.update(books_id - 1, form.data)   # books  = books.get(books_id)
           books.save_all()
           return redirect(url_for('update'))
    return render_template("update.html", form=form, books_id=books_id,books=books.all())
#________________________________________________________________________________________________________

@app.route ("/remove")
def remove():                   
    return render_template('remove.html',  books=books.all())

@app.route ("/remove/<int:books_id>")
def afterremove(books_id):  
    print(books_id)
    position = books.get(books_id)
    books.remove(position)
    books.save_all()        
    return redirect(url_for('remove'))#nazwa metody  tu l 38

 

