from random import sample


def optimize(n, m, price: [list, ...]):
    C = [[float("inf") if i * j == 0 else 0 for j in range(m + 1)] for i in range(n + 1)]
    C[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            C[i][j] = min(C[i][j - 1], C[i - 1][j], C[i - 1][j - 1]) + price[i][j]

    path = []
    i = n
    j = m
    while (i, j) != (0, 0):
        path.append((i, j))
        prev_C = min(C[i][j - 1], C[i - 1][j], C[i - 1][j - 1])
        if C[i][j - 1] == prev_C:
            i, j = i, j - 1
        elif C[i - 1][j] == prev_C:
            i, j = i - 1, j
        else:
            i, j = i - 1, j - 1

    return C[-1][-1], path[::-1]


def main():
    n, m = map(int, input().split())
    price = [sample(range(9), k=(m + 1)) for i in range(n + 1)]
    print(*optimize(n, m, price))


if __name__ == "__main__":
    main()
