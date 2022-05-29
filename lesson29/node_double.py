class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def get_previous(self):
        return self._previous

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next

    def set_previous(self, new_previous):
        self._previous = new_previous
