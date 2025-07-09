class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, title):
        book_to_remove = None
        for book in self.books:
            if book.title == title:
                book_to_remove = book
                #print('found ' + book_to_remove)

        if book_to_remove is not None:
            self.books.remove(book_to_remove)

library = Library()

hobbit = Book('The Hobbit', 'J.R.R. Tolkien')
library.add(hobbit)

fellowship = Book('The Fellowship of the Rings', 'J.R.R. Tolkien')
library.add(fellowship)

print('BEFORE')
for book in library.books:
    print(book)

library.remove('The Hobbit')

print('AFTER')
for book in library.books:
    print(book)
