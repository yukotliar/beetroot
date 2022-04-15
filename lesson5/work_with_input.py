# Створити модуль для роботи з різними типами даних, що вводяться з клавіатури
# 1. Звичайне читання
# 2. Читання цілих чисел
# 3. Читання десяткових чисел
# 4. Читання тексту та розділення його на слова (за розділовими знаками ".", ",", "-")
# 5. Читання списку чисел розділених комами (поєднати перетворення на ціле та десяткове)


def input_str(additional_text):
    return input(additional_text)


def input_integer(additionnal_text):
    return int(input(additionnal_text))


def input_float(additionnal_text):
    return float(input(additionnal_text))


def input_text(additionnal_text):
    result = input(additionnal_text)
    result = result.replace('.', ' ').replace(',', ' ').replace('-', ' ').replace('  ', ' ')
    return result.split(' ')


def input_numbers(additionnal_text):
    result = input(additionnal_text)
    result = result.split(',')
    i = 0
    while i < len(result):
        if '.' in result[i]:
            result[i] = float(result[i])
        else:
            result[i] = int(result[i])
        i += 1
    return result