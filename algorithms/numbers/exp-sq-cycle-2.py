def pow(a, n):
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