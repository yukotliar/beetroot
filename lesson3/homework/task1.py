# String manipulation
# Write a Python program to get a string made of the first 2
# and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
string = input('Enter your string: ')
if len(string) > 1:
    print(string[:2]+string[-2:])
else:
    print('Empty String')