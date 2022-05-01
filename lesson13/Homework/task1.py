# Write a Python program to detect the number of local variables declared in a function.

def test_func():
    test_variable1, test_variable2, test_variable3, test_variable4 = 123, 54.645, 'Test', ['tomato', 'racoon', 'snake']

print(test_func.__code__.co_nlocals)