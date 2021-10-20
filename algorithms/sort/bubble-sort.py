def bubble_sort(a):
    for step in range(len(a) - 1):
        for i in range(len(a) - 1 - step):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]


massive = list(map(int, input().split()))
bubble_sort(massive)
print(*massive)
