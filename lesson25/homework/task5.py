def sum_of_digits(digit_string):
    try:
        if int(digit_string) == 0:
            return 0
        return (int(digit_string) % 10 + sum_of_digits(int(digit_string) / 10))
    except ValueError:
        raise ValueError("input string must be digit string")

print(sum_of_digits('26'))
print(sum_of_digits('test'))