def asc(a: list):
    f = [0] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j] and f[j] > f[i]:
                f[i] = f[j]
        f[i] += 1

    maxind = f.index(max(f))
    subseq = [a[maxind]]
    for i in range(maxind - 1, -1, -1):
        if f[i] == f[maxind] - 1:
            subseq.append(a[i])
            maxind = f.index(f[i])

    return subseq[::-1]


a = list(map(int, input().split()))
print(*asc(a))
