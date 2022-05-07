# Створити декоратор, який буде виводити інформацію про назву функції, її внутрішні методи, використання пам'яті,
# максимальне значення використання пам'яті та час потрібний на її виконання

from functools import wraps
import tracemalloc
from time import perf_counter


def info(func):
    @wraps(func)
    def show(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        func(*args, **kwargs)
        main, pick = tracemalloc.get_traced_memory()
        end = perf_counter()
        print(f'Function name {func.__name__}')
        print(f'Docstring {func.__doc__}')
        print(f'Memory usage {main / 10**6:.6f} MB')
        print(f'Pick usage {pick / 10**6:.6f} MB')
        print(f'Time {end - start:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return show


@info
def make_list1():
    """Range"""
    my_list = list(range(100000))


@info
def make_list2():
    """List comprehension"""
    my_list = [l for l in range(100000)]


@info
def make_list3():
    """Append"""
    my_list = []
    for item in range(100000):
        my_list.append(item)


@info
def make_list4():
    """Concatenation"""
    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


make_list1()
make_list2()
make_list3()
make_list4()

