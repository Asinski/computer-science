def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastpos = 0
    lastsym = s[0]
    ans = []
    for i in range(1, len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))

    return ''.join(ans)


s = input()
print(rle(s))
