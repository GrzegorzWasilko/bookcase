import json

class Books:
    def __init__(self):# konstruktor objektu klasy
        try:
            with open("books.json", "r") as f:
                self.books= json.load(f) #tworzę zmienną books do której zapisuje dane z pliku json
        except FileNotFoundError:
            self.books = [] #jak nie ma pliku json to powstanie pusta lista 

    def all(self):#wyswietla liste
        return self.books

    def get(self, id):# podaje element o podanym elemencie  id w liście
        return self.books[id]

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False
        
    def remove(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False


 
        