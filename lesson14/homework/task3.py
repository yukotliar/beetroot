# Write a decorator `arg_rules` that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
#
# max_length: 15
#
# type_: str
#
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.

def arg_rules(value, type_, words):
    def inner(func):
        def wrap(*args):
            phrase = func(*args)
            print(phrase)
            print(len(phrase))
            print(type(phrase))
            if len(value) > len(phrase):
                raise ValueError(f"hey you, your length shouldn't be grater than {value}")

            if type_ != type(phrase):
                raise TypeError(f"cmon we need a {type_} here")

            for word in words:
                if word not in phrase:
                    raise ValueError(f'{word} is not in')
                else:
                    return phrase

        return wrap

    return inner


@arg_rules(15, 'str', ['Steve', '30'])
def hello(name):
    print(f"Hello! My name is {name}', I'm 30 years old.")


hello('Steve')
