def anagrams(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    return d


s1 = input()
s2 = input()
d1 = anagrams(s1)
d2 = anagrams(s2)

print("YES") if d1 == d2 else print("NO")