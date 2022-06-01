# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

from lesson27.stack import Stack

correspondence_matrix = {'(':')',
                         '{':'}',
                         '[':']'}

stack1 = Stack()
stack2 = Stack()
while True:
    sequence = input('enter your sequence one by one or "continue" to proceed: ')
    if sequence == 'continue':
        break
    else:
        if sequence in '({[':
            stack1.push(sequence)
        elif sequence in ')}]':
            stack2.push(sequence)
if stack1.size() != stack2.size():
    print('inbalanced')
    quit()
for index in range(stack1.size()):
    if correspondence_matrix[stack1.pop()] == stack2.pop():
        pass
    else:
        print('inbalanced')
print('balanced')

