# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers

import random

iterator, random_list1, random_list2 = 0, [], []

while iterator < 10:
    random_list1.append(random.randrange(1, 11))
    random_list2.append(random.randrange(1, 11))
    iterator += 1

list_without_duplicates = set(random_list1 + random_list2)
print(list_without_duplicates)
