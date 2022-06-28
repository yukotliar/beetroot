def mult(a: int, n: int) -> int:
    if a == 0 or n == 0:
        return 0
    elif a < 0 or n < 0:
        raise ValueError("This function works only with postive integers")
    return a + mult(a, n - 1)

print(mult(2, 4))
print(mult(2, 0))
print(mult(2, -4))