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

    def remove_positives(self, integers):
        return [int for int in integers if int >= 0]

    def filter_leaps(self, integers):
        return list(filter(lambda int: int % 4 == 0 or int % 100 == 0 and int % 400 != 0, integers))


example = Attributes()
list1 = [int for int in range(-9, 10, 3)]
list2 = [int for int in range(1991, 2022)]
print(example.square_nums(list1))
print(example.remove_positives(list1))
print(example.filter_leaps(list2))
