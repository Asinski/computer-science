def optimize(n, m):
    F = [[1 if i * j == 0 else 0 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = F[i][j - 1] + F[i - 1][j] + F[i - 1][j - 1]

    return F[-1][-1]


def main():
    n, m = map(int, input().split())
    print(optimize(n, m))


if __name__ == "__main__":
    main()
