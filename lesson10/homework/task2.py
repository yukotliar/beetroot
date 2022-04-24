# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).
def function():
    try:
        a, b = float(input('Enter a: ')), float(input('Enter b: '))
        print(a ** 2 / b)
    except ValueError:
        print('You\'re trying to enter string, please, enter int or float value.')
    except ZeroDivisionError:
        print('That\'s not math math analysis, you can\'t divide by zero here.')


function()
