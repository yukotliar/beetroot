# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function
def in_range(end, start=0, step=1):
    while end > start:
        yield start
        start += step


my_range = in_range(9, 2, 2)
for i in my_range:
    print(i)

for i in range(2, 9, 2):
    print(i)