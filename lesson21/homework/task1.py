# Релізувати контекстний менеджер для open() за допомогою функцій та декоратора
from contextlib import contextmanager


@contextmanager
def open_file(in_file, mode):
    try:
        file = open(in_file, mode)
        yield file
    except Exception as exc:
        print(exc)
    finally:
        try:
            file.close()
        except:
            yield None


with open_file('test.txt', 'r') as myfile:
    if myfile:
        print(myfile.read())