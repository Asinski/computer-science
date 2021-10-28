from stack import Stack


def sort_train(n: int, trains: list):
    trains = trains[::-1]
    depo = Stack()
    for train in range(1, n + 1):
        if train in trains:
            while trains[-1] != train:
                depo.push(trains.pop())
            depo.push(trains.pop())
        if depo.peek() == train:
            depo.pop()
        else:
            return False
    else:
        return True


count_trains = int(input())
sample_trains = list(map(int, input().split()))
print(sort_train(count_trains, sample_trains))
