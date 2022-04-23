# При введенні числових даних часто зустрічається типова проблема: користувач вводить текст замість чисел.
# При спробі перетворити дані в int генерується виняток TypeError. Напишіть функцію, яка приймає два числа,
# шукає їх суму і виводить результат. Перехопіть виняток TypeError, якщо будь-яке із вхідних значень не є числом,
# і виведіть зручне повідомлення про помилку. Протестуйте функцію: спочатку введіть два числа,
# а потім введіть текст замість одного з чисел.

def sum_result(value1, value2):
    try:
        print(int(value1) + int(value2))
    except (ValueError, TypeError):
        print('Wrong values are entered. Please, enter only int values.')


if __name__ == '__main__':
    while True:
        sum_result(input('Enter first value: '), input('Enter second value: '))
