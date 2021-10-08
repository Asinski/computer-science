def edit_distance(str1, str2, m, n):
    if not m:
        return n
    elif not n:
        return m
    elif str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)
    return 1 + min(edit_distance(str1, str2, m, n - 1),
                   edit_distance(str1, str2, m - 1, n),
                   edit_distance(str1, str2, m - 1, n - 1))


s1 = input()
s2 = input()
print(edit_distance(s1, s2, len(s1), len(s2)))
