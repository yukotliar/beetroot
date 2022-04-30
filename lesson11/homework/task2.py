# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application,
# else raise an error. After the user exits, all data should be saved to loaded JSON.
import json

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


def print_result(results):
        print(f'Контакт {results["first_name"]} {results["last_name"]} з номером {results["phone"]} '
              f'проживає в {results["country"]} {results["city"]}')


def save_data(data):
    with open('data.json', 'r') as data_file:
        try:
            database = json.load(data_file)
            with open('data.json', 'w') as data_file:
                database.append(data)
                json.dump(database, data_file, indent=2)
                print('Контакт збережено')
        except json.decoder.JSONDecodeError:
            print('Ваша база даних не валідна')


def search(command, request):
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


def delete(phone):
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


def update(phone):
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
