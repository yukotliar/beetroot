# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.
import email

from lesson17.homework.task2 import Author, Library, Book
from unittest import TestCase


class TestLib(TestCase):
    def setUp(self) -> None:
        self.lib = Library('Libre')
        self.aut1 = Author('John', 'USA', '05.06.1901')
        self.aut2 = Author('Clark', 'Sweden', '04.03.1912')
        self.aut3 = Author('Jane', 'UK', '06.07.1921')

    def test_add_book(self):
        self.lib.new_book('Love', 1921, self.aut1)
        self.lib.new_book('Soul', 1941, self.aut3)
        self.lib.new_book('Fate', 1922, self.aut1)
        self.lib.new_book('Sun', 1933, self.aut2)
        self.lib.new_book('Hope', 1922, self.aut2)
        self.assertTrue('Love' and 'Soul' in str(self.lib.books), 'Books added')

    def test_book_amount(self):
        self.assertEqual(Book.amount, 5, 'Same amount')

    def test_group_by_author(self):
        self.lib.new_book('Love', 1921, self.aut1)
        self.lib.new_book('Soul', 1941, self.aut3)
        self.lib.new_book('Fate', 1922, self.aut1)
        self.lib.new_book('Sun', 1933, self.aut2)
        self.lib.new_book('Hope', 1922, self.aut2)
        aut1_filter = str(self.lib.group_by_author(self.aut1))
        self.assertTrue('Love' and 'Fate' in aut1_filter, 'Filtered correctly')

    def test_group_by_year(self):
        self.lib.new_book('Love', 1921, self.aut1)
        self.lib.new_book('Soul', 1941, self.aut3)
        self.lib.new_book('Fate', 1922, self.aut1)
        self.lib.new_book('Sun', 1933, self.aut2)
        self.lib.new_book('Hope', 1922, self.aut2)
        year_filter = str(self.lib.group_by_year(1922))
        self.assertTrue('Hope' and 'Fate' in year_filter, 'Filtered correctly')
