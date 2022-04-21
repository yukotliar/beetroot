# Створіть таблицю множення на конкретне число.
# 1 * 1 = 1
# 2 * 1 = 2
# 3 * 1 = 3
# 4 * 1 = 4
# .........

def table(number):
    for i in range(11):
        print(f'{number} * {i} = {int(number) * i}')


while True:
    number = input('Please, submit your number or Q for QUIT: ')
    if number.upper() == 'Q':
        break
    else:
        table(number)
