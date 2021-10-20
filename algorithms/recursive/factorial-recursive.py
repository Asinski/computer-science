def factorial(n):
    return 1 if n == 1 else factorial(n - 1) * n


n = int(input())
print(factorial(n))
