# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.
import string
import random

test_list = [random.choices(string.ascii_uppercase) for i in range(9)]


def iterable(sequence, action):
    iterator = iter(sequence)
    completed_iterating = False
    while not completed_iterating:
        try:
            action(next(iterator))
        except StopIteration:
            completed_iterating = True


iterable(test_list, print)
