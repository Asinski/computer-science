class LinkedList:

    def __init__(self):
        self.begin = None

    def insert(self, x):
        self.begin = [x, self.begin]

    def pop(self):
        x = self.begin[0]
        self.begin = self.begin[1]
        return x
