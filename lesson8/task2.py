# Реалізуйте шифр Цезаря. Один з перших відомих прикладів шифрування був використаний Юлієм Цезарем.
# Цезар надавав письмові вказівки своїм генералам, але він не бажав, зрозуміло, щоб про них знали вороги.
# У результаті він створив власне шифрування, що згодом стало відоме як шифр Цезаря.
# Ідея цього шифру проста (і, як наслідок, вона не забезпечує серйозного захисту).
# Кожна буква в оригінальному повідомленні зміщується на 3 позиції.
# В результаті A стає D, B стає E, C стає F, D стає G і т. д.
# Останні три букви у алфавіті повертаються до початку: X стає A, Y стає B, а Z стає C.
# Нелітерні символи не враховуються шифром. Користувач вводить з клавітури повідомлення та зсув,
# а потім програма відображає зашифроване повідомлення. Переконайтеся, що програма шифрує як великі та малі літери.
# Програма також повинна підтримувати значення негативних зсувів, щоб її можна було використовувати як
# для кодування повідомлень, так і для декодування повідомлень.
# У нагоді стануть такі функції: ord() (перетворює символ у номер позиції цього символу у таблиці ASCII )
# і chr() (перетворює номер позиції символу у таблиці ASCII у відповідний символ).

# coder function
def mess_coder(text, offset):
    result = []
    offset = int(offset)
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122: # for lowwer case a - z
            if ord(text[i]) + offset <= 122:
                result.append(chr(int(ord(text[i]) + offset)))
            else:
                result.append(chr(int(ord(text[i]) + offset - 122 + 96)))
        elif 65 <= ord(text[i]) <= 90: # for upper case A - Z
            if ord(text[i]) + offset <= 90:
                result.append(chr(int(ord(text[i]) + offset)))
            else:
                result.append(chr(int(ord(text[i]) + offset - 90 + 64)))
        else:
            result.append(text[i])
    return ''.join(result)

# decoder function
def mess_decoder(text, offset):
    result = []
    offset = int(offset)
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122: # for lowwer case a - z
            if ord(text[i]) - offset >= 97:
                result.append(chr(int(ord(text[i]) - offset)))
            else:
                result.append(chr(int(ord(text[i]) - offset + 122 - 96)))
        elif 65 <= ord(text[i]) <= 90: # for upper case A - Z
            if ord(text[i]) - offset >= 65:
                result.append(chr(int(ord(text[i]) - offset)))
            else:
                result.append(chr(int(ord(text[i]) - offset + 90 - 64)))
        else:
            result.append(text[i])
    return ''.join(result)


while True:

    script_type = input('C - to write and CODE new message, D - to read and DECODE the message, Q - for QUIT: ')

    if script_type.upper() == 'C' or script_type.upper() == 'D':
        offset_number = input('Offset (positive integer): ')

        if offset_number.isdigit() and int(offset_number) % 1 == 0 and int(offset_number) > 0:
            message = input('Your message: ')

            if script_type.upper() == 'C':
                print(f'Coded message: {mess_coder(message, offset_number)}')

            elif script_type.upper() == 'D':
                print(f'Decoded message: {mess_decoder(message, offset_number)}')

        else:
            print('Please, input only positive integer')
            continue

    elif script_type.upper() == 'Q':
        print('See you next time! Bye!')
        break

    else:
        print('Please, choose only C to CODE or D to DECODE your message')
        continue

