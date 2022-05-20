# Reimplement Fraction class from Lesson17-3 homework using dataclass approach

from dataclasses import dataclass


@dataclass
class Fraction:
    value: float

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


x = Fraction(1 / 2)

y = Fraction(1 / 4)

x + y == Fraction(3 / 4)

print(x + y)
print(x * y)
print(x / y)
print(x - y)
