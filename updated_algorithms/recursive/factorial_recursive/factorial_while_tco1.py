def factorial_while_tco1(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


assert factorial_while_tco1(2) == 2
assert factorial_while_tco1(3) == 6
assert factorial_while_tco1(4) == 24
