# A Person class
#
# Make a class called Person. Make the __init__() method take firstname, lastname,
# and age as parameters and add them as attributes. Make another method called talk()
# which makes prints a greeting from the person containing, for example like this:
# “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self, firstname, lastname, age):
        print(f'Hello, my name is {firstname} {lastname} and I’m {age} years old')


person1 = Person('Carl', 'Johnson', 26)
person1.talk(person1.firstname, person1.lastname, person1.age)
