def bancomat(len_chop, nominal=(5, 10, 20, 50, 100)):
    """
    Алгоритм для поиска оптимального количества банкнот для выдачи нужной суммы.
    Сложность определяется суммой len_chop и количеством банкнот len(nominal).
    + len(nominal) для большого количества банкнот (в этом случае лучше использовать алгоритм с предками).
    """
    F = [0] + [float("inf")] * len_chop
    prev = [-1] * (len_chop + 1)
    for k in range(1, len_chop + 1):
        for i in range(len(nominal)):
            if k - nominal[i] >= 0 and F[k - nominal[i]] < F[k]:
                F[k] = F[k - nominal[i]]
                prev[k] = nominal[i]
        F[k] += 1

    bancnotes = []
    k = len_chop
    while k > 0:
        # for i in range(len(nominal)):
        #     if k - nominal[i] >= 0 and F[k] == F[k - nominal[i]] + 1:
        #         bancnotes.append(nominal[i])
        #         k -= nominal[i]
        bancnotes.append(prev[k])
        k -= prev[k]

    return sorted(bancnotes)


chop = int(input())
print(*bancomat(chop))
