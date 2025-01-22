import random


def reservoir_sampling(stream, k):
    reservoir = []

    for i, element in enumerate(stream):
        if i < k:
            reservoir.append(element)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = element

    return reservoir


stream = [10, 20, 30, 40, 50, 60]
k = 2
print(reservoir_sampling(stream, k))
