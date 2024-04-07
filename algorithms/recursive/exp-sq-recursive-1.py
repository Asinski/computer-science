def pow(a, n):
    if n == 0:
        return 1
    p = pow(a * a, n // 2)
    if n % 2:
        p *= a
    return p


a, n = map(int, input().split())
print(pow(a, n))
