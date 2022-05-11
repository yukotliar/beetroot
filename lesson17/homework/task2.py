# Library
#
# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
#
# 2) Book - name, year, author (author must be an instance of Author class)
#
# 3) Author - name, country, birthday, books = []
#
# Library class
#
# Methods:
#
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
# list for the current library.
#
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
#
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#
# All 3 classes must have a readable __repr__ and __str__ methods.
#
# Also, the book class should have a class variable which holds the amount of all existing books

class Library:  # Library - name, books = [], authors = []
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):  # returns an instance of Book class and adds the book to the books
        # list for the current library.
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        Book.amount += 1

    def group_by_author(self, author):  # returns a list of all books grouped by the specified author
        aut_filter = []
        for book in self.books:
            if book.author.name == author.name:
                aut_filter.append(book)
        return aut_filter

    def group_by_year(self, year):  # returns a list of all the books grouped by the specified year
        year_filter = []
        for book in self.books:
            if book.year == year:
                year_filter.append(book)
        return year_filter

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Book:  # Book - name, year, author (author must be an instance of Author class)
    amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f' The book called {self.name}, released at {self.year}, it\'s author name is {self.author}'

    def __str__(self):
        return f' The book called {self.name}, released at {self.year}, it\'s author name is {self.author}'


class Author:  # Author - name, country, birthday, books = []
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return f'{self.name} from {self.country} born {self.birthday}'

    def __str__(self):
        return f'{self.name} from {self.country} born {self.birthday}'

lib = Library('Libre')

aut1 = Author('John', 'USA', '05.06.1901')
aut2 = Author('Clark', 'Sweden', '04.03.1912')
aut3 = Author('Jane', 'UK', '06.07.1921')

lib.new_book('Love', 1921, aut1)
lib.new_book('Fate', 1922, aut1)
lib.new_book('Hope', 1922, aut2)
lib.new_book('Sun', 1933, aut2)
lib.new_book('Soul', 1941, aut3)

print(lib.group_by_author(aut1))

print(lib.group_by_year(1922))

print(Book.amount)

print(lib)