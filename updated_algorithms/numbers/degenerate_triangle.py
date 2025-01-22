def degenerate_triangle(a, b, c):
    return "YES" if a < (b + c) and b < (a + c) and c < (a + b) else "NO"


assert degenerate_triangle(3, 4, 5) == "YES"
assert degenerate_triangle(3, 4, 7) == "NO"
assert degenerate_triangle(3, 4, 8) == "NO"
assert degenerate_triangle(3, 4, 9) == "NO"
assert degenerate_triangle(3, 4, 10) == "NO"
