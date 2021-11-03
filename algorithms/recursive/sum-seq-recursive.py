def sum_recursive(n):
    return 1 if n == 1 else n + sum_recursive(n - 1)


n = int(input())
print(sum_recursive(n))
