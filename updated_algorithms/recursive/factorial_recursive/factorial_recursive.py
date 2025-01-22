def factorial_recursive(n):
    return 1 if n == 1 else factorial_recursive(n - 1) * n


assert factorial_recursive(2) == 2
assert factorial_recursive(3) == 6
assert factorial_recursive(4) == 24
