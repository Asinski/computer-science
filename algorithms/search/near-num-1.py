def near_number(n, seq, x):
    num = seq[0]
    diff = abs(x - seq[0])
    for i in range(1, n):
        if abs(x - seq[i]) < diff:
            num = seq[i]
            diff = abs(x - seq[i])

    return num


assert near_number(5, [1, 2, 3, 4, 5], 6) == 5
assert near_number(5, [5, 4, 3, 2, 1], 3) == 3


def main():
    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())
    print(near_number(n, seq, x))


if __name__ == '__main__':
    main()
