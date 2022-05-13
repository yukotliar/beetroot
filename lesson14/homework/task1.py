# Write a decorator that prints a function with arguments passed to it.
#
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapped(*args):
        print(func)
    return wrapped


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(10, 20)

square_all(10, 20, 30, 40, 50)
