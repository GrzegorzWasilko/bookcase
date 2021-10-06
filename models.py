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

    def get(self, id):# podaje element o podanym elemencie  id
        return self.books[id]

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
        
    def remove(self,id):
        print(self.books)
        data = self.books[id]    # albo data = self.get[id]
        
        self.books.remove(data)
        self.save_all()
