def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    elif n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x


x, n = map(int, input().split())
print(power(x, n))
