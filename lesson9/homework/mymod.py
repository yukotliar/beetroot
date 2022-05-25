def count_lines(name):  # function that reads an input file and counts the number of lines in it
    with open(f'{name}.txt') as file:
        return len(file.readlines())

def count_chars(name):  # function that reads an input file and counts the number of characters in it
    with open(f'{name}.txt') as file:
        return len(file.read().rstrip())

def test(name):  # function that calls both counting functions with a given input filename.
    return count_lines(name), count_chars(name)