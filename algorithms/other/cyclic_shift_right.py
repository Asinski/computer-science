def cyclic_shift_right(a, n):
    tmp = a[n - 1]
    for k in range(n - 2, -1, -1):
        a[k + 1] = a[k]
    a[0] = tmp

    return a


n = int(input())
a = list(map(int, input().split()))
print(*cyclic_shift_right(a, n))
