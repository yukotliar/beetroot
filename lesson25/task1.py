# Task 1. Check if a number is Palindrome.
# Перевіряємо чи два крайні елементи рівні, якщо так викликаємо в середині функцію з новим значенням (без 1 і останнього символу)
# Додаємо перевірку на довжину <= 2 -> повертаємо результат
# І якщо елементи не рівні, зупиняємо перевірку передаємо результат

def palindrom(value):
    if value[0] == value[-1]:
        if len(value) <= 2 and value[0] == value[-1]:
            return True
        else:
            return palindrom(value[1:-1])
    else:
        return False


print(palindrom('2020201020202'))