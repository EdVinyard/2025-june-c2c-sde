class Library:
    def __init__(self):
        self.books = {} ## book ID ==> Book instance

    def add(self, id, title):
        self.books[id] = title

    def remove(self, id):
        del self.books[id]

    def print(self):
        for id, title in self.books.items():
            print(id, title)

library = Library()
library.add(123, 'The Hobbit')
library.add(456, 'The Fellowship of the Rings')

print('BEFORE')
library.print()

library.remove(123)

print('AFTER')
library.print()
