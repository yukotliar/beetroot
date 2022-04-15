# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
#
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string
import random

from lesson5.work_with_input import *

entered_string = input_str('Enter your string: ')
for i in range(5):
    for i in range(len(entered_string)):
        print(random.choice(entered_string), end='')
    print(' ', end='')
