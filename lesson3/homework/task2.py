# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and
# is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
phone_number = input('Enter valid phone number: ')
if len(phone_number) == 10 and phone_number.isnumeric():
    print('Entered phone number seems to be valid')
else:
    print('Entered phone number has less than 10 or has alphabetic characters')