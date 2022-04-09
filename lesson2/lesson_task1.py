x, y, R = int(input()), int(input()), int(input())
if R ** 2 > x ** 2 + y ** 2:
    print('this spot is in the circle')
elif R ** 2 == x ** 2 + y ** 2:
    print('this spot is on the circle')
else:
    print('this spot is out the circle')