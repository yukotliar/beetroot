# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers
import random

iterator, random_list = 0, []

while iterator < 10:
    random_list.append(random.randrange(1, 1000))
    iterator += 1

print(max(random_list))
