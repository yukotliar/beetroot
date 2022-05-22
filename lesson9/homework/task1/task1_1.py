# Imports practice
#
#  Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

import string
import random
from task1_2 import with_index

test_list = [random.choices(string.ascii_uppercase) for i in range(9)]

my_enum = with_index(test_list, 2)
for i in my_enum:
    print(i)