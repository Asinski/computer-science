def bancomat(len_chop, nominal=(1, 2, 5, 10, 20, 50, 100)):
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
    tmp = len_chop
    while tmp > 0:
        # for i in range(len(nominal)):
        #     if tmp - nominal[i] >= 0 and F[tmp] == F[tmp - nominal[i]] + 1:
        #         bancnotes.append(nominal[i])
        #         tmp -= nominal[i]
        bancnotes.append(prev[tmp])
        tmp -= prev[tmp]

    return sorted(bancnotes)


assert bancomat(6) == [1, 5]
assert bancomat(10) == [10]
assert bancomat(170) == [20, 50, 100]


def main():
    chop = int(input())
    print(*bancomat(chop))


if __name__ == "__main__":
    main()
