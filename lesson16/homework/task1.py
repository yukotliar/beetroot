# School
#
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, gender, age, name):
        self.gender = gender
        self.age = age
        self.name = name

    def who(self, gender, age, name):
        print(f'I\'m {age}, my name is {name}, and gender is {gender})


class Student(Person):
    def __init__(self, gender, age, name, grade):
        super.__init__(gender, age, name)
        self.grade = grade

    def what_grade(self, grade):
        print(f'I\'m studying in {grade} grade')


class Teacher(Person):
    def __init__(self, gender, age, name, subject, rate, hours):
        super.__init__(gender, age, name)
        self.rate = rate
        self.subject = subject
        self.hours = hours

    def how_much(self, rate, hours):
        monthly = rate * hours
        print(f'My monthly salary is {monthly}')
