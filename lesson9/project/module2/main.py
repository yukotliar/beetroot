import os

file_path = os.path.dirname(os.path.abspath(__file__)).replace('module2', 'module1/data_folder/')

with open(os.path.join(file_path, 'file.txt'), 'r') as file:
    print(file.read())