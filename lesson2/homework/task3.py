# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b,
# then print the result for each of the following:
# Addition, Subtraction, Division, Multiplication, Exponent (Power), Modulus, Floor division
a, b = float(input('enter a value: ')), float(input('enter b value: '))
print('Addition: ' + str(a + b), 'Subtraction: ' + str(a - b), 'Division: ' + str(a / b), 'Multiplication: ' + str(a * b), \
      'Exponent: ' + str(pow(a, b)), 'Modulus: ' + str(a % b), 'Floor division: ' + str(a // b))
