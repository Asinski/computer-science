class Sequence:
    previous = None
    type = None

    def __init__(self, seq):
        if seq:
            for item in seq:
                self.add(item)

    def add(self, newnum):
        if self.previous:
            if newnum == self.previous:
                if self.type is None:
                    self.type = 'CONSTANT'
                elif self.type == 'ASCENDING':
                    self.type = 'WEAKLY ASCENDING'
                elif self.type == 'DESCENDING':
                    self.type = 'WEAKLY DESCENDING'
            elif newnum > self.previous:
                if self.type is None:
                    self.type = 'ASCENDING'
                elif self.type == 'WEAKLY DESCENDING' or self.type == 'DESCENDING':
                    self.type = 'RANDOM'
                elif self.type == 'CONSTANT':
                    self.type = 'WEAKLY ASCENDING'
            else:
                if self.type is None:
                    self.type = 'DESCENDING'
                elif self.type == 'WEAKLY ASCENDING' or self.type == 'ASCENDING':
                    self.type = 'RANDOM'
                elif self.type == 'CONSTANT':
                    self.type = 'WEAKLY DESCENDING'

        self.previous = newnum


def main():
    sequence = Sequence([])
    while True:
        newnum = int(input())
        if newnum == -2000000000:
            print(sequence.type)
            break
        sequence.add(newnum)


if __name__ == '__main__':
    main()
