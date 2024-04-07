def optimize(cb, m, w):
    F = [[0] * (cb + 1) for _ in range(len(m))]
    for i in range(1, len(m)):
        for j in range(cb + 1):
            if j >= m[i]:
                F[i][j] = max(F[i - 1][j], F[i - 1][j - m[i]] + w[i])
            else:
                F[i][j] = F[i - 1][j]

    things = []
    tmp = cb
    for i in range(len(m) - 1, 0, -1):
        if F[i][tmp] != F[i - 1][tmp]:
            things.append((m[i], w[i]))
            tmp -= m[i]

    return things[::-1]


assert optimize(12, [0, 7, 3, 1, 5, 4], [0, 10, 4, 2, 6, 7]) == [(7, 10), (1, 2), (4, 7)]


def main():
    capacity_backpack = int(input())
    mass = [0] + list(map(int, input().split()))
    worth = [0] + list(map(int, input().split()))
    print(*optimize(capacity_backpack, mass, worth))


if __name__ == "__main__":
    main()
