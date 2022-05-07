class Person:
    education_level = 0

    def __init__(self, f_name, s_name):
        self.f_name = f_name
        self.s_name = s_name

    @property
    def education(self):
        return self.education_level

    @education.setter
    def education(self, value):
        self.education_level = value

    @education.deleter
    def education(self):
        del self.education_level


class School:

    def __init__(self, person):
        self.person = person
        check = School.check_level(self.person)
        if check:
            self.person.education_level += 1

    @classmethod
    def check_level(cls, person):
        cls.person = person
        if cls.person.education_level == 0:
            return True
        else:
            print('Not ok')
            return False


class Student:

    def __init__(self, person):
        self.person = person
        check = Student.check_level(self.person)
        if check:
            self.person.education_level += 1

    @classmethod
    def check_level(cls, person):
        cls.person = person
        if cls.person.education_level == 1:
            return True
        else:
            print('Not ok')
            return False


a = Person('Serhii', 'Matsur')

b = Person('Ivan', 'Dorn')

School(a)
School(b)
Student(b)

print(a.education_level)
print(b.education_level)