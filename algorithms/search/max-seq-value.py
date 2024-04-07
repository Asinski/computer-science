def findmax(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = seq[i]

    return ans
