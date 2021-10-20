def asc(seq):
    prev = seq[0]
    for i in range(1, len(seq)):
        if prev >= seq[i]:
            return 'NO'
        prev = seq[i]
    return 'YES'


def main():
    seq = list(map(int, input().split()))
    print(asc(seq))


if __name__ == '__main__':
    main()
