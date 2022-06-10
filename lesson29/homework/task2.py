from lesson29.node import Node


class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode._next = self.head
            self.head = newnode

    def pop(self):

        if self.isempty():
            return None

        else:
            poppednode = self.head
            self.head = self.head._next
            poppednode._next = None
            return poppednode._data

    def display(self):

        iternode = self.head
        if self.isempty():
            print("It's empty")

        else:

            while (iternode != None):
                print(iternode._data, "->", end=" ")
                iternode = iternode._next
            return


TestStack = Stack()
TestStack.push(10)
TestStack.push(11)
TestStack.push(12)
TestStack.push(13)
TestStack.pop()
TestStack.display()