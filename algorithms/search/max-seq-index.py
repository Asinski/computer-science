def findmax(seq):
    ans = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i

    return seq[ans]
