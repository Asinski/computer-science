

def select_sort(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]


massive = list(map(int, input().split()))
select_sort(massive)
print(massive)

