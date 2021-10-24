def edit_distance(a: str, b: str, m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    elif a[m - 1] == b[n - 1]:
        return edit_distance(a, b, m - 1, n - 1)
    return 1 + min(edit_distance(a, b, m, n - 1),
                   edit_distance(a, b, m - 1, n),
                   edit_distance(a, b, m - 1, n - 1))


a = input()
b = input()
print(edit_distance(a, b, len(a), len(b)))
