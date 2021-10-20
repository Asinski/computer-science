def findx(seq, x):
    ans = -1
    for i in range(len(seq) - 1, -1, -1):
        if ans == -1 and seq[i] == x:
            ans = i

    return ans
