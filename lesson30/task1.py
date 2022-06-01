def peak(sample: list):
    l = 0
    r = len(sample) - 1
    found = False
    mid = int((l + r) / 2)
    while not found:
        if sample[mid-1] < sample[mid] > sample[mid+1]:
            found = True
            result = sample[mid]
        elif sample[mid-1] > sample[mid+1]:
            mid -= 1
        else:
            mid += 1
    return result


a = [5, 10, 20, 15]

b = [1, 2, 2, 23, 90, 67]

print(peak(a))
print(peak(b))