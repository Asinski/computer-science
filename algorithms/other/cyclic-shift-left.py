

def cyclic_shift_left(a, n):

    tmp = a[0]
    for k in range(n - 1):
        a[k] = a[k + 1]
    a[n - 1] = tmp

    return a


n = int(input())
a = list(map(int, input().split()))
print(*cyclic_shift_left(a, n))
