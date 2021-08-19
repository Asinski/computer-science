def anagrams(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


s1 = input()
s2 = input()
d1 = anagrams(s1)
d2 = anagrams(s2)

print("YES") if d1 == d2 else print("NO")
