# Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка,
# і записує у текстовий файл інформацію, щодо парності або непарності числа.
d = open('result.txt', 'a+')
while True:
    a = input('Введіть число: ')
    if a == 'Q':
        break
    elif int(a) % 2 == 0:
        c = ' = even number'
    else:
        c = ' = odd number'
    print(str(a) + c, file=d)