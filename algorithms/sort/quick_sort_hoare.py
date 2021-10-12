from random import randint


def quick_sort(n):
    if len(n) <= 1:
        return n

    elem = n[randint(0, len(n) - 1)]
    left = list(filter(lambda x: x < elem, n))
    center = [i for i in n if i == elem]
    right = list(filter(lambda x: x > elem, n))

    return quick_sort(left) + center + quick_sort(right)


massive = list(map(int, input().split()))
print(*quick_sort(massive))
