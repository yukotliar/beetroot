# Custom exception
#
# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file
import time


class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message

    def log(self):
        logs = open('logs.txt', 'a', encoding='utf-8')
        localtime = time.localtime()
        current_time = time.strftime("%H:%M:%S", localtime)
        logs.write(str(current_time) + ' ' + self.message + '\n')
        logs.close()


error = MyCustomError('We have a problem')
error.log()
