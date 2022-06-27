def to_power(x, exp):
    if exp <= 0:
        raise ValueError('This function works only with exp > 0.')
    if exp == 1:
        return x
    if exp % 2 == 0:
        return to_power(x, exp // 2) * to_power(x, exp // 2)
    return to_power(x, exp - 1) * x


print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))
