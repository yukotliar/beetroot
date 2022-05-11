# Створити декоратор який записує час та дату виконання функції. Вивід інформації має містити назву функції та дату
# і час у форматі hh:mm dd-mm-yy. Використати бібліотеку datetime.

import datetime


def dt(func):
    now = datetime.datetime.now()
    print(f'Date and time: {now.strftime("%HH:%MM %dd-%mm")}. Function name: {func.__name__}')


@dt
def some_func():
    pass
