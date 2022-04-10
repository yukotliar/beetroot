# Check whether the point belongs to a circle with center at the origin
# or whether it lies outside the circle line or in the middle.
x, y, R = int(input()), int(input()), int(input())
if R ** 2 > x ** 2 + y ** 2:
    print('this point is in the circle')
elif R ** 2 == x ** 2 + y ** 2:
    print('this point is on the circle')
else:
    print('this point is out the circle')