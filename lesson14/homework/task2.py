# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
from functools import wraps


def stop_words(words):

    def decorator(func):
        def wrap(*args):
            phrase = func(*args)
            new_phrase = ''
            split_phrase = phrase.split(' ')
            for word in split_phrase:
                if word in words:
                    word = '*'
                new_phrase += ' ' + word
            print(new_phrase)

        return wrap

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# def replace_words(list):
#     list = list()
#     phrase = 'Say hello to clear water'
#     new_phrase = ''
#     split_phrase = phrase.split(' ')
#     for i in split_phrase:
#         if i in list:
#             i = '*'
#         new_phrase += ' ' + i
#     print(new_phrase.lstrip())
#
# @replace_words
# def stop_list():
#     stop_list = ['hello', 'water']
#     return stop_list
