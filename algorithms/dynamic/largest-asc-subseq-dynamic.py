def asc(a: list):
    F = [0] * len(a)
    # prev = [-1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j] and F[j] > F[i]:  # >=
                F[i] = F[j]
                # prev[i] = j
        F[i] += 1

    ind = F.index(max(F))
    gis = [a[ind]]
    # while prev[ind] != -1:
    #     ind = prev[ind]
    #     gis.append(a[ind])
    while F[ind] > 1:
        j = ind - 1
        while a[j] >= a[ind] or F[j] != F[ind] - 1:
            j -= 1
        gis.append(a[j])
        ind = j

    return gis[::-1]


a = list(map(int, input().split()))
print(*asc(a))
