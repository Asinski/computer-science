def pow(a, n):
    b = a
    k = n
    p = 1
    while k:
        if k % 2 == 0:
            k //= 2
            b *= b
        else:
            k -= 1
            p *= b
    return p


a, n = map(int, input().split())
print(pow(a, n))
