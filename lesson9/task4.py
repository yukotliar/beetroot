# Task 4. Написати дві функції що генерують списки різними методами, та затосувати до них функцію timein.repeat
import timeit


setup = "from math import sqrt"


func1 = """def func1():
                for i in range(1000):
                    return i * sqrt(i)"""


time = timeit.repeat(setup=setup, stmt=func1, repeat=3, number=10000)

print(time)