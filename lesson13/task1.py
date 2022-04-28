# Написати програму яка містить набір базових команд на копм'ютері (копіювати, вставити, вирізати,
# знайти, надрукувати)
# Зчитувати у користувача конктретну команду і виводити повідомлення на екран. Не використовувати if.


def copy():
    print('copy')


def paste():
    print('paste')


def cut():
    print('cut')


def find():
    print('find')


def print_():
    print('print')


func_dict = {
    'copy': copy,
    'paste': paste,
    'cut': cut,
    'find': find,
    'print': print_
}

command = input('Enter your command: ')

try:
    func_dict[command]()
except:
    print('wrong input')
