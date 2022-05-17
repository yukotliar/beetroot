# Створити клас База даних, що має 4 атрибути: назву, пароль та список дат підключень, і параметер що
# відповідає за її наповнення. Створити контекстний менеджер для роботи з базою данних - відкриття бази,
# підключення, запис даних та її закриття.

from datetime import date

today = date.today()


class Database:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.connection = None
        self.dates = []
        self.table = []
        self.access_name = 'admin'
        self.access_pass = 'admin'

    def __enter__(self):
        if self.name == self.access_name and self.password == self.access_pass:
            self.dates.append(today.strftime("%d/%m/%Y"))
            return self
        else:
            return print('Not authorised')

    def input_data(self, value):
        self.table.append(value)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


with Database('admin', 'admins') as db:
    db.input_data('some data')

print(db.dates, db.table)
