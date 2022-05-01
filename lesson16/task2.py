# Створити калькулятор площі багатокутників

class NFigure:
    def __init__(self, sides, len_, ap):
        self.sides = sides
        self.len_ = len_
        self.ap = ap

    def square(self):
        return 0.5 * self.len_ * self.ap