# Розширити написаний калькулятор добавивши до нього обробники помилок.
def make_operation(operator, *args):
    # немає перевірки на пусті параметри
    if operator == '+':  # TypeError коли str + int
        return sum(args)
    if operator == '-':
        result = args[0]  # TypeError коли беремо індекс від числа
        for i in range(len(args) - 1):
            result -= args[i + 1]  # IndexError якщо в циклі конкретне число (range)
        return result
    if operator == '*':
        result = 1
        for arg in args:
            result *= arg
        return result
    else:
        print('Wrong operator, just + or - or *')
def checkout_error(number_list):
    try:
        for number in number_list:
            for symbol in ['[', ']', '(', ')', ',', '*']:
                if symbol in number:
                    raise TypeError
        for i in range(len(number_list)):
            if number_list[i].isalpha():
                raise ValueError
            else:
                number_list[i] = float(number_list[i])
    except TypeError:
        print('Введені дані є некоректиними')
        return []
    except ValueError:
        print('Не можемо перетворити символ у рядок')
        return []
    else:
        return number_list
if __name__ == '__main__':
    try:
        numbers = input('Введіть кількість аргументів: ')
        if numbers.isalpha():
            raise ValueError
        list_ = [input(f'Введіть {i + 1} аргумент: ') for i in range(int(numbers))]
        operator = input('Введіть оператор: ')
        list_ = checkout_error(list_)
        print(make_operation(operator, *list_))
    except ValueError:
        print('Ви ввели рядок замість числа')