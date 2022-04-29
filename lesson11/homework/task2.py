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
        pass
    elif command in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
        search(command, input('Введіть запит для пошуку: '))
    elif command == 'up':
        pass
    elif command == 'del':
        delete(input('Введіть номер телефону: '))
    elif command == 'exit':
        pass
    else:
        print('Введена вами команда не коректна')


def print_result(results):
    for result in results:
        print(f'Контакт {result["first_name"]} {result["last_name"]} з номером {result["phone"]} '
              f'проживає в {result["country"]} {result["city"]}')


def save_data(data):
    with open('data.json', 'r') as data_file:
        database = json.load(data_file)
    with open('data.json', 'w') as data_file:
        database.append(data)
        json.dump(database, data_file, indent=2)


def search(command, request):
    with open('data.json', 'r') as data_file:
        database = json.load(data_file)
    if command == 'sfl':
        for item in database:
            if item['first_name'] + ' ' + item['last_name'] == request:
                return item
            else:
                return 'За вашим запитом нічого не знайдено'
    else:
        for item in database:
            if item[search_data[command]] == request:
                return item
            else:
                return 'За вашим запитом нічого не знайдено'


def delete(phone):
    with open('data.json', 'r') as data_file:
        database = list(json.load(data_file))
    with open('data.json', 'w') as data_file:
        for item in database:
            if item['phone'] == phone:
                database.remove(item)
                json.dump(database, data_file, indent=2)
            else:
                return 'За вашим запитом нічого не знайдено'

if __name__ == '__main__':
    # save_data(input_contact())
    read_commands()
