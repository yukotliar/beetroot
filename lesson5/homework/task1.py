# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated. The result should be sent back to the user via a print statement.
import math
import random

from lesson5.work_with_input import *

player_value = input_integer('Enter int value from 1 to 10: ')
generated_value = random.randrange(1, 10)
if player_value == generated_value:
    print('You win!')
else:
    print('You lose!')
