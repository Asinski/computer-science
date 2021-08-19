def matrix_mul_p(a, b):
    return [sum(x * y for x, y in zip(row_b, b)) for row_b in a]


def matrix_mul_b(a, b):
    return [[sum(x * y
                 for x, y in zip(row_b, col_b))
             for col_b in b]
            for row_b in a]


def pow(n):
    b = [[0, 1],
         [1, 1]]
    p = [0, 1]
    while n:
        if n % 2:
            p = matrix_mul_p(b, p)
        b = matrix_mul_b(b, b)
        n //= 2
    return p


def fibonacci(n):
    return pow(n)[0]


n = int(input())
print(fibonacci(n))