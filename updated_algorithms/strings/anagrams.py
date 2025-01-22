from collections import defaultdict


# Подсчитывай и сравнивай - O(n)

def anagrams11(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


def anagrams12(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    return d


def anagrams13(s):
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    return d


def anagrams14(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    are_they_anagrams = True
    while j < 26 and are_they_anagrams:
        if c1[j] == c2[j]:
            j += 1
        else:
            are_they_anagrams = False

    return are_they_anagrams


# Сортируй и сравнивай - O(nlogn)

def anagrams21(s1, s2):
    return sorted(s1) == sorted(s2)


def anagrams22(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    are_they_anagrams = True

    while pos < len(s1) and are_they_anagrams:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            are_they_anagrams = False

    return are_they_anagrams


# Полный перебор - O(n!)


# Метки - O(n2)

def anagrams31(s1, s2):
    alist = list(s2)

    pos1 = 0
    are_they_anagrams = True

    while pos1 < len(s1) and are_they_anagrams:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            are_they_anagrams = False

        pos1 += 1

    return are_they_anagrams
