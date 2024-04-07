def pow(a, n):
    if n < 0:
        n = -n
        a = 1. / a
    b = a
    p = 1
    while n:
        if n % 2:
            p *= b
        b *= b
        n //= 2
    return p


a, n = map(int, input().split())
print(pow(a, n))