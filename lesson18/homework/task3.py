# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible):
#
# methods:
#
# to_int
#
# to_str
#
# to_bool
#
# to_float

from functools import wraps


class TypeDecorators:

    def to_int(func):
        @wraps(func)
        def inner(*args):
            try:
                return int(func(*args))
            except:
                return None

        return inner

    def to_bool(func):
        @wraps(func)
        def inner(*args):
            try:
                return bool(func(*args))
            except:
                return None

        return inner

    def to_str(func):
        @wraps(func)
        def inner(*args):
            try:
                return str(func(*args))
            except:
                return None

        return inner

    def to_float(func):
        @wraps(func)
        def inner(*args):
            try:
                return float(func(*args))
            except:
                return None

        return inner


@TypeDecorators.to_int
def make_int(string: str):
    return string
w

@TypeDecorators.to_bool
def make_bool(string: str):
    return string


@TypeDecorators.to_float
def make_float(string: str):
    return string


@TypeDecorators.to_str
def make_str(string: int | float | bool):
    return string


print(type(make_int('25')))
assert make_int('25') == 25

print(type(make_bool('True')))
assert make_bool('True') is True

print(type(make_float('25.25')))
assert make_float('25.25') == 25.25

print(type(make_str(25)))
assert make_str(25) == '25'
