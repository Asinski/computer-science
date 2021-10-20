def combinations(n, k):
    flat_nk = [[1] + [0] * k for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            flat_nk[i][j] = flat_nk[i - 1][j] + flat_nk[i - 1][j - 1]

    return flat_nk[n][k]


n, k = map(int, input().split())
print(combinations(n, k))
