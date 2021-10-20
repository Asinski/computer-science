from prettytable import PrettyTable, ALL

triangle_Pascal = PrettyTable(header=False, hrules=ALL)

n = int(input())
triangle = [([1] + [0] * n) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in range(0, n + 1):
    triangle_Pascal.add_row([triangle[i][j] if triangle[i][j] != 0 else f"" for j in range(0, n + 1)])

triangle_Pascal.align = "l"
print(triangle_Pascal)
