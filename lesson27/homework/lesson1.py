# Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

stack = []
while True:
    sequence = input('enter your sequence one by one or "print" to proceed: ')
    if sequence == 'print':
        break
    else:
        stack.append(sequence)
for index in range(len(stack)):
    print(stack.pop())