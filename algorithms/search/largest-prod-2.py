def max_product(seq):
    if len(seq) == 2:
        return sorted(seq)

    max_pos = None
    max2_pos = None
    max_neg = None
    max2_neg = None

    for num in seq:
        if num < 0:
            if max_neg is None or num < max_neg:
                max2_neg = max_neg
                max_neg = num
            elif max2_neg is None or num < max2_neg:
                max2_neg = num
        else:
            if max_pos is None or num > max_pos:
                max2_pos = max_pos
                max_pos = num
            elif max2_pos is None or num > max2_pos:
                max2_pos = num

    pos_prod = max_pos * max2_pos if max_pos and max2_pos else float("-inf")
    neg_prod = max_neg * max2_neg if max_neg and max2_neg else float("-inf")

    return sorted([max_pos, max2_pos]) if pos_prod > neg_prod else \
        sorted([max_neg, max2_neg])


def main():
    seq = list(map(int, input().split()))
    print(*max_product(seq))


if __name__ == '__main__':
    main()
