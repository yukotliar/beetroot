# Mathematician
#
# Implement a class Mathematician which is a helper class for doing math operations on lists
#
# The class doesn't take any attributes and only has methods:
#
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers)
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years')

class Attributes:

    def square_nums(self, integers):
        return [int ** 2 for int in integers]


example = Attributes()
list = [int for int in range(10)]
print(example.square_nums(list))
