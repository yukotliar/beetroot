# Practise type annotations
#
# Go to your implementation of the Phonebook application from module 1 or any other comprehensive code,
# which you have done during the course, and annotate this code with type hints, using knowledge from this lesson.
import json
from typing import *

new_data = {
    "first_name": "",
    "last_name": "",
    "phone": "",
    "city": "",
    "country": ""
}

search_data = {
    "sf": "first_name",
    "sl": "last_name",
    "sp": "phone",
    "sct": "city",
    "sc": "country"
}

field_names = ["ім'я", "прізвище", "номер телефону", "місто", "країну"]


def input_contact():
    our_data = new_data.copy()
    for key, name in zip(our_data.keys(), field_names):
        our_data[key] = input(f'Введіть {name}: ')
    return our_data


def read_commands():
    print("Достпуні команди:",
          "n - створити новий запис",
          "sf - пошук за ім'ям",
          "sl - пошук за прізвищем",
          "sfl - пошук за повним ім'ям",
          "sp - пошук за телефоном",
          "sct - пошук за містом",
          "sc - пошук за країною",
          "up - оновення запису",
          "del - видалити запис",
          "exit - вихід з програми", sep='\n')
    command = input('Введіть команду: ')
    if command == 'n':
        save_data(input_contact())
    elif command in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
        try:
            print_result(search(command, input('Введіть запит для пошуку: ')))
        except TypeError:
            print('За вашим запитом нічого не знайдено')
    elif command == 'up':
        update(input('Введіть номер телефону: '))
    elif command == 'del':
        delete(input('Введіть номер телефону: '))
    elif command == 'exit':
        quit()
    else:
        print('Введена вами команда не коректна')


def print_result(results: Any):
    print(f'Контакт {results["first_name"]} {results["last_name"]} з номером {results["phone"]} '
          f'проживає в {results["country"]} {results["city"]}')


def save_data(data: Dict):
    with open('data.json', 'r') as data_file:
        try:
            database = json.load(data_file)
            with open('data.json', 'w') as data_file:
                database.append(data)
                json.dump(database, data_file, indent=2)
                print('Контакт збережено')
        except json.decoder.JSONDecodeError:
            print('Ваша база даних не валідна')


def search(command: str, request: str):
    with open('data.json', 'r') as data_file:
        database = json.load(data_file)
    if command == 'sfl':
        for item in database:
            if item['first_name'] + ' ' + item['last_name'] == request:
                return item
    else:
        for item in database:
            if item[search_data[command]] == request:
                return item


def delete(phone: str):
    with open('data.json', 'r') as data_file:
        database = json.load(data_file)
    with open('data.json', 'w') as data_file:
        for item in database:
            if item['phone'] == phone:
                database.remove(item)
                json.dump(database, data_file, indent=2)
                print('Контакт видалено')
            else:
                print('За вашим запитом нічого не знайдено')


def update(phone: str):
    print("Доступні для оновлення параметри:",
          "sf - ім'я",
          "sl - прізвище",
          "sp - телефон",
          "sct - місто",
          "sc - країна", sep='\n')
    command = input('Введіть параметр: ')
    new_value = input('Введіть новий параметр: ')
    with open('data.json', 'r') as data_file:
        database = json.load(data_file)
    with open('data.json', 'w') as data_file:
        for item in database:
            if item['phone'] == phone:
                item[search_data[command]] = new_value
                json.dump(database, data_file, indent=2)
                print('Дані збережено')


if __name__ == '__main__':
    read_commands()
