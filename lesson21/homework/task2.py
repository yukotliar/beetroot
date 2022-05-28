# Writing tests for context manager
#
# Take your implementation of the context manager class from Task 1 and write tests for it.
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors or you have errors in the runtime context suite.

from unittest import TestCase
from task1 import OpenFile

class TestOpenFile(TestCase):
    def setUp(self):
        self.file_name = 'test.txt'
        self.new_file = 'new.txt'
        self.unexisting_file = 'test2.txt'
        self.read_mode = 'r'
        self.write_mode = 'w'

    def test_file_isnt_empty(self):
        with OpenFile(self.file_name, self.read_mode) as file:
            self.assertTrue(len(file.read()) > 0)

    def test_counter(self):
        with OpenFile(self.file_name, self.read_mode):
            self.assertEqual(OpenFile.counter, 1)

    def test_file_creation(self):
        with OpenFile(self.new_file, self.write_mode) as file:
            file.write('Test')
        with OpenFile(self.new_file, self.read_mode) as file:
            self.assertEqual(file.read(), 'Test')

