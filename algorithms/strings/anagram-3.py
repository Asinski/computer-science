from collections import defaultdict


def anagrams(s):
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    return d

