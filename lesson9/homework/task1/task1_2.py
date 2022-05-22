def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start + i, iterable[i]