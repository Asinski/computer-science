from collections import defaultdict


def anagrams(s):
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    return d


s1 = input()
s2 = input()
d1 = anagrams(s1)
d2 = anagrams(s2)

print("YES") if d1 == d2 else print("NO")