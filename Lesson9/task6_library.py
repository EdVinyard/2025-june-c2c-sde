class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book):
        self.books.remove(book)
        self.borrowed.append(book)

    def return_book(self, book):
        self.borrowed.remove(book)
        self.books.append(book)

    def display_books(self):
        print('In the library:')
        for book in self.books:
            print('- ' + book)

        print('Borrowed:')
        for book in self.borrowed:
            print('- ' + book)

library = Library()
library.add_book('The Lord of the Rings')
library.add_book('The Hobbit')
library.add_book('The Silmarillion')
library.borrow_book('The Hobbit')
library.borrow_book('The Lord of the Rings')
library.return_book('The Hobbit')
library.display_books()
