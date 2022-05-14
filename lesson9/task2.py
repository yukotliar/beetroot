# Task 2. my_module.py.
# - Run the file directly with Python: python my_module.py
# - Invoke the module with -m flag: python -m my_module
# - Import the module from another Python file: python -c "import my_module"
# - Import and call the function defined: python -c "import my_module; my_module.my_function()"
# my_module.py
print('This will run when the file is imported.')

def my_function():
    print('Executing function. This will only run when the function is called.')

if __name__ == '__main__':
    print('This will get executed only if')
    print('the module is invoked directly.')
    print('It will not run when this module is imported')
    my_function()