def degenerate_triangle(a, b, c):
    return "YES" if a < (b + c) and b < (a + c) and c < (a + b) else "NO"


a, b, c = map(int, input().split())
print(degenerate_triangle(a, b, c))
