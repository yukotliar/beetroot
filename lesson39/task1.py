from threading import Lock, Condition


class Boat:
    def __init__(self):
        self.boatlocation = True  # T for left bank, F for right
        self.boatcount = 0
        self.mutex = Lock()
        self.leftbank = Condition(self.mutex)
        self.rightbank = Condition(self.mutex)
