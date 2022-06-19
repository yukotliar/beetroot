# Implement binary search using recursion.
def binary_search(array, low, high, x):

	if high >= low:
		mid = (high + low) // 2
		if array[mid] == x:
			return mid
		elif array[mid] > x:
			return binary_search(array, low, mid - 1, x)
		else:
			return binary_search(array, mid + 1, high, x)
	else:
		return -1

array = [ 1, 6, 8, 10, 65, 4, 10 ]
x = 10

result = binary_search(array, 0, len(array)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
