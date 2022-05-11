# Створити генератор текстових емоджі. Емоджі мають починатись там закінчуватись дужками одного й того самого типу,
# в середині містити 3 рандомних символи !@#$^*_-=+?/,.:;~.

import random

def emodgy():
    strings = "!@#$^*_-=+?/,.:;~"
    grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]
    while True:
        symb = ''
        for i in range(3):
            symb += strings[random.randint(0, len(strings) - 1)]
        brackets = grouped_strings[random.randint(0, 3)]
        emodgy = brackets[0] + symb + brackets[1]
        yield emodgy


a = emodgy()

for i in range(50):
    print(next(a))