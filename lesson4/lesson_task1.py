# Write a program to display the names of countries in capital letters
# which also includes checking the end of the work on the keyword
# and skip the output if equal to another keyword
while True:
    country = input('Enter your county: ')
    if country == 'russia':
        continue
    elif country == 'q':
        break
    else:
        print(country.capitalize())
