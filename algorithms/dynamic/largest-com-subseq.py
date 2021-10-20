def lcs(a: list, b: list):
    f = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    subseq = []
    i = len(a)
    j = len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            subseq.append(a[i - 1])
            i -= 1
            j -= 1
        elif f[i - 1][j] == f[i][j]:
            i -= 1
        else:
            j -= 1

    return subseq[::-1]


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*lcs(a, b))
