def optimize(cb, gb):
    F = [1] + [0] * cb
    prev = [-1] * (cb + 1)
    for i in range(len(gb)):
        for j in range(cb, gb[i] - 1, -1):
            if F[j - gb[i]] == 1:
                F[j] = 1
                prev[j] = gb[i]

    tmp = cb
    while not F[tmp]:
        tmp -= 1

    bars = []
    while tmp > 0:
        bars.append(prev[tmp])
        tmp -= prev[tmp]

    return bars[::-1]


assert optimize(14, [3, 5, 7, 10]) == [3, 10]


def main():
    capacity_bags = int(input())
    gold_bars = list(map(int, input().split()))
    print(optimize(capacity_bags, gold_bars))


if __name__ == "__main__":
    main()
