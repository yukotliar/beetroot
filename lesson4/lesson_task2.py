# Write a python program, which sums all digits in a python string.
# Examples, input - '1234', output - 10
# Check the presence of symbols in the string
while True:
    number = input('Enter your number: ')
    iterator, sum_ = 0, 0
    while iterator < len(number):
        if number[iterator].isdigit():
            sum_ += int(number[iterator])
        else:
            iterator += 1
            continue
        iterator += 1
    print(f'Sum of the entered string {number} is {sum_}')