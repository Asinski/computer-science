def asc(a: list):
    F = [-float("inf")] + [float("inf")] * (len(a) + 1)
    for i in range(len(a)):
        left = 0
        right = len(a) + 1
        while right - left > 1:
            middle = (left + right) // 2
            if F[middle] >= a[i]:
                right = middle
            else:
                left = middle
        F[right] = a[i]

    length_subseq = len(a) + 1
    while F[length_subseq] == float("inf"):
        length_subseq -= 1

    return length_subseq


a = list(map(int, input().split()))
print(asc(a))
