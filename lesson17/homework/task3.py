# Fraction
#
# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *)
# with appropriate checking and error handling

class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other_value):
        return Fraction(self.value + other_value.value)

    def __mul__(self, other_value):
        return Fraction(self.value * other_value.value)

    def __truediv__(self, other_value):
        return Fraction(self.value / other_value.value)

    def __sub__(self, other_value):
        return Fraction(self.value - other_value.value)

    def __str__(self):
        return str(self.value)

x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)

print(x + y)
print(x * y)
print(x / y)
print(x - y)