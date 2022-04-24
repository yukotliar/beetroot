# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError? The program shows the IndexError first,
# and then the KeyError as well.
def oops():
    raise IndexError


def another_function(word='bear'):
    try:
        print(word[4])
    except:
        oops()


another_function()
