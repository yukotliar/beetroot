# cтворити клас Student, який має два базових атрибути що описують студента, property що вопертає його
# повне ім'я, staticmethod який для кожного студента повертає один і той самий університет,
# а також classmetod який повертає назву класу та прізвище студента

class Student:
    first_name = 'John'
    second_name = 'Conor'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.second_name}'

    @staticmethod
    def get_uni():
        return 'Random University'

    @classmethod
    def class_name(cls):
        return f'Hello from class: {cls.__name__}, second name: {cls.second_name}'


student1 = Student()
print(student1.get_full_name)
print(student1.get_uni())
print(student1.class_name())
