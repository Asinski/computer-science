def combinations(n, k):
    """
    Сочетания, или биномиальные коэффициенты, или количество неупорядоченных выборок без повторений
    """
    C = [[1] + [0] * k for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            C[i][j] = C[i - 1][j] + C[i - 1][j - 1]

    return C[n][k]


n, k = map(int, input().split())
print(combinations(n, k))
