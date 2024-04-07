def insertion_sort(a):
    for i in range(1, len(a)):
        item_to_insert = a[i]
        j = i - 1
        while j >= 0 and a[j] > item_to_insert:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = item_to_insert


massive = list(map(int, input().split()))
insertion_sort(massive)
print(*massive)
