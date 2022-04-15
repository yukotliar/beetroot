# The math quiz program
#
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.
from lesson5.work_with_input import *

import math

print('Hello, human! This program is made to test your factorial calculation skills.')
value = input_integer('Enter any int value: ')
user_answer = input_integer('Enter its factorial: ')
if math.factorial(value) == user_answer:
    print('That\'s correct. You\'re pure genius!')
else:
    print('Sorry, your answer is wrong.')