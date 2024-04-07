def fibonacci(n):
    fib = [0, 1] + [0] * (n - 2)
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib


n = int(input())
print(fibonacci(n))
