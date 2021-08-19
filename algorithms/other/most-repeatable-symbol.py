s = input()
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = dct.get(now, 0) + 1
    # dct[now] += 1
for key in dct:
    if dct[key] > anscnt:
        anscnt = dct[key]
        ans = key
print(ans)