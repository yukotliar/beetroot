# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
# is a valid email string.

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Email:
    def __init__(self, email):
        if (re.fullmatch(regex, email)):
            self.email = email
            print("valid email")
        else:
            raise ValueError('entered email is invalid')


ron = Email('ronald@gmail.com')
ben = Email('@gmail.com')