import json

class BooksForm :
    def __init__(self):# konstruktor objektu klasy
        try:
            with open("books.json", "r") as f:
                self.books= json.load(f) #tworzę zmienną books do której zapisuje dane z pliku json
        except FileNotFoundError:
            self.books = [] #jak nie ma pliku json to powstanie pusta lista 

    def all(self):#wyswietla liste
        return self.books

    def get(self, id):
        book = [book for book in self.all() if book['id'] == id]
        if book:
            return book[0]
        return []

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.books[id] = data
        self.save_all()
        
    def remove(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False


"""def update(self, id, data):
        book = self.get(id)
        if book:
            index = self.books.index(book)
            self.books[index] = data
            self.save_all()
            return True
        return False"""
 
        