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
    if request.method == "POST":            #sprawdza czy walidacje (metody) sie powiodły 
        if form.validate_on_submit():       #spr czy dane do form zostały poprawnie wpisane .
            books.create(form.data)         # dopisuje do objektu.klasyBooks dane z formularza
            books.save_all()               # zapisuje stan pliku json 
        return redirect(url_for('index')) #wracam do index

    return render_template('index.html', form=form, books=books.all())# get powoduje wyswietlenie form i listy z books
#________________________________________________________________________________________________________________
@app.route ("/update")
def ChoseUpdate():  
    form = Library()            
    return render_template('update.html',form=form, books=books.all())




###_______________________________________________________________________________________________________

@app.route ("/remove")
def remove():   
    j=0                
    return render_template('remove.html',j=j,  books=books.all())
###
@app.route ("/remove/<int:id>")
def afterremove(id):  

    if request.method == "POST":
        book = books.get(id )
        form = Library(data=book)
        if form.validate_on_submit():
            books.remove(id - 1, form.data)
            return redirect(url_for('remove'))#nazwa metody  
###_____________________________________________________________________________________________________

 
