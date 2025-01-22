def factorial_tail_recursive(n, current_result=1):
    return current_result if n == 0 else factorial_tail_recursive(n - 1, current_result * n)


assert factorial_tail_recursive(2) == 2
assert factorial_tail_recursive(3) == 6
assert factorial_tail_recursive(4) == 24
