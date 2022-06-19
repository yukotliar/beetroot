# Read about the Fibonacci search and implement it using python.
# Explore its complexity and compare it to sequential, binary searches.
def fibonacci_search(list, target):
    size = len(list)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size - 1)
        if list[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif list[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (list[size - 1] == target):
        return size - 1
    return None

list = list(range(101))
print(fibonacci_search(list, 9))
print(fibonacci_search(list, 99))
print(fibonacci_search(list, 999))