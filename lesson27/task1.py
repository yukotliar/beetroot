# Converting Decimal Numbers to Binary Numbers

from stack import Stack


def binary(number):
    result = Stack()
    bin_num = ''
    while number:
        index = number % 2
        result.push(index)
        number = number // 2
    for i in range(int(result.size())):
        bin_num += str(result.pop())
    return bin_num



print(binary(2))
print(binary(10))
print(binary(35))