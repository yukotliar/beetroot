# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”
from lesson5.work_with_input import *

name, age = input_str('Enter your name: '), input_integer('Enter your age: ')
print(f'Hello {name}, on your next birthday you’ll be {age + 1} years')
