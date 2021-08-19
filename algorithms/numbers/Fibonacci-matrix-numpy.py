import numpy as np


def pow(n):
    b = np.array([[0, 1], [1, 1]], dtype=np.float64)
    p = np.array([0, 1], dtype=np.float64)
    while n:
        if n % 2:
            p = np.dot(b, p)
        b = np.dot(b, b)
        n //= 2
    return p


def fibonacci(n):
    return pow(n)[0]


n = int(input())
print(fibonacci(n))