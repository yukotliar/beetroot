# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def rectangle_square(a, b):
    s = a * b
    print(f'Square of a rectagle is {s}')


def rectangle_perimeter_square(a, b):
    p = 2 * (a + b)
    print(f'Perimeter of a rectagle is {p}')
    return rectangle_square(a, b)

rectangle_perimeter_square(1, 2)