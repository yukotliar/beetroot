from dequeu import Deque


def palindrom(text: Deque):
    sample = Deque()
    for i in range(len(text)):
        sample.add_front(text[i])
    while sample.size() > 1:
        rear = sample.remove_rear()
        front = sample.remove_front()
        if str(rear).upper() == str(front).upper():
            continue
        else:
            print(f'The word "{text}" is not palindrom, because {rear} != {front} ')
            return False
    print(f'The word "{text}" is palindrom!')
    return True


palindrom('Radar')
palindrom('Mother')
palindrom('jklkMj')
palindrom('toottoot')