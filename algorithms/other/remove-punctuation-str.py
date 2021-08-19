from string import punctuation


s = input()
s_wo_p = ''
for char in s:
    if char not in punctuation:
        s_wo_p += char

print(s_wo_p)
