from queue import Queue


def queue_hospital(aged):
    window_1 = Queue()
    window_2 = Queue()
    for i in range(len(aged)):
        window_1.push(i) if aged[i] == 1 else window_2.push(i)

    times = dict.fromkeys(range(len(aged)), 0)

    tw1 = 0
    while not window_1.isempty():
        to_two = window_1.pop()
        times[to_two] += (5 + tw1)
        window_2.push(to_two)
        tw1 += 5

    tw2 = 0
    while not window_2.isempty():
        if aged[window_2.top()] == 1:
            if tw2 == 0:
                times[window_2.pop()] += 5
            else:
                times[window_2.pop()] += tw2
        else:
            times[window_2.pop()] += (5 + tw2)
            tw2 += 5

    return times.values()


aged = list(map(int, input().split()))
print(*queue_hospital(aged))
