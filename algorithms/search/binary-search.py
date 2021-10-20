def left_border(seq, num):
    left = -1
    right = len(seq)
    while right - left > 1:
        middle = (left + right) // 2
        if seq[middle] < num:
            left = middle
        else:
            right = middle

    return left


def right_border(seq, num):
    left = -1
    right = len(seq)
    while right - left > 1:
        middle = (left + right) // 2
        if seq[middle] <= num:
            left = middle
        else:
            right = middle

    return right


def binary_search(seq, num):
    lb = left_border(seq, num)
    rb = right_border(seq, num)
    return None if rb - lb == 1 \
        else (seq[:rb] if lb == -1 else (seq[lb + 1:] if rb == len(seq) else seq[lb + 1:rb]))


num = int(input())
seq = sorted(list(map(int, input().split())))
print(binary_search(seq, num))
