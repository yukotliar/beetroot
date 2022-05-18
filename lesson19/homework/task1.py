# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
import string
import random


def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start + i, iterable[i]


test_list = [random.choices(string.ascii_uppercase) for i in range(9)]

my_enum = with_index(test_list, 2)
for i in my_enum:
    print(i)

py_enum = enumerate(test_list, 2)
for i in py_enum:
    print(i)
