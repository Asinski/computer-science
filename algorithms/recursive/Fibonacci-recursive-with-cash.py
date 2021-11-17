F = [None] * 10_000


def fibonacci(n):
    assert (0 <= n < 10_000)
    if F[n] is None:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return F[n]


n = int(input())
print(fibonacci(n))
