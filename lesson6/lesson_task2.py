# Напишіть програму, яка запитує в користувача логін та пароль.
# Якщо вони вірні, повертає користувачеві два випадкових числа (ключ доступу та id) та зберігає їх. Мають бути незмінні.
# Якщо не вірні, замінити значення на 0.
import random

login, password = 'login', 'password'
if login == 'login' and password == 'password':
    credential = (random.random(), random.random())
else:
    credential = (0, 0)
