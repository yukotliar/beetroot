# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration
import random

iterator, numbers_list, exceptions_list = 1, [], []

while iterator < 101:
    numbers_list.append(iterator)
    if iterator % 7 == 0 and iterator % 5 != 0:
        exceptions_list.append(iterator)
    iterator += 1
print(exceptions_list)
