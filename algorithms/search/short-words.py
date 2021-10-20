def shortwords(words):
    minlen = len(words[0])
    for word in words[1:]:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    for word in words:
        if len(word) == minlen:
            ans.append(word)

    return ' '.join(ans)
