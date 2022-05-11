# Створити декоратор-клас, який буде обмежувати кількість викликів функції
# та виводити порядковий номер виклику

class Limiter:

    def __init__(self, func, limit=3):
        self.func = func
        self.call_count = 0
        self.limit = limit

    def __call__(self, *args, **kwargs):
        self.limit = args[1]
        if self.call_count <= self.limit:
            self.call_count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'Function {self.func.__name__} stopped, limit - {self.limit} ')


@Limiter
def say_hello_to_putin(text):
    print(f'Hello, {text}')


text = 'Huilo'

say_hello_to_putin(text)
say_hello_to_putin(text)
say_hello_to_putin(text)
say_hello_to_putin(text)