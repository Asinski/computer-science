import math


def max_product(seq):
    if len(seq) == 3:
        return seq

    min_neg = [None, None, None]
    max_neg = [None, None]
    max_pos = [None, None, None]

    for num in seq:
        if num < 0:
            if max_neg[0] is None or num < max_neg[0]:
                max_neg[1] = max_neg[0]
                max_neg[0] = num
            elif max_neg[1] is None or num < max_neg[1]:
                max_neg[1] = num

            if min_neg[2] is None or num > min_neg[2]:
                min_neg[0] = min_neg[1]
                min_neg[1] = min_neg[2]
                min_neg[2] = num
            elif min_neg[1] is None or num > min_neg[1]:
                min_neg[0] = min_neg[1]
                min_neg[1] = num
            elif min_neg[0] is None or num > min_neg[0]:
                min_neg[0] = num
        else:
            if max_pos[2] is None or num > max_pos[2]:
                max_pos[0] = max_pos[1]
                max_pos[1] = max_pos[2]
                max_pos[2] = num
            elif max_pos[1] is None or num > max_pos[1]:
                max_pos[0] = max_pos[1]
                max_pos[1] = num
            elif max_pos[0] is None or num > max_pos[0]:
                max_pos[0] = num

    three_pos = max_pos \
        if len(list(filter(lambda x: x, max_pos))) == 3 \
        else -math.inf
    two_neg_one_pos = [*max_neg, max_pos[2]] \
        if max_pos[2] is not None and len(list(filter(lambda x: x, max_neg))) == 2 \
        else -math.inf
    three_min_neg = min_neg if len(list(filter(lambda x: x, min_neg))) == 3 \
        else -math.inf

    return max([three_pos, two_neg_one_pos, three_min_neg], key=math.prod)


def main():
    seq = list(map(int, input().split()))
    print(*max_product(seq))


if __name__ == '__main__':
    main()
