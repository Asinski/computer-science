def near_number(seq):
    num1 = 0
    num2 = 0
    min_diff = abs(seq[1] - seq[0]) + 1
    for i in range(1, len(seq)):
        for j in range(i):
            if abs(seq[i] - seq[j]) < min_diff:
                min_diff = abs(seq[i] - seq[j])
                num1 = seq[j]
                num2 = seq[i]

    return num1, num2


def main():
    seq = list(map(int, input().split()))
    print(near_number(seq))


if __name__ == '__main__':
    main()
