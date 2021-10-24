def boyer_moore_horspool(s: str, sb: str, ls: int, lsb: int):
    """
    Алгоритм Бойера-Мура-Хорспула поиска подстроки в строке.
    Сложность: O(N * M) - худшая, 0(M / N) - лучшая, а в общем случае - 0(M / |Σ|), где |Σ| - мощность множества сигма,
    в которое входят символы строки и образа.
    Возвращает индекс(ы) строки, с которого(ых) начинается подстрока.
    """
    if not (ls and lsb):
        return None

    # предобработка образа: создание массива d, который будет содержать величины сдвигов
    d = dict.fromkeys([chr(i) for i in range(1104)], lsb)
    i = lsb - 2
    while i >= 0:
        if d[sb[i]] != lsb:
            i -= 1
            continue
        else:
            d[sb[i]] = lsb - (i + 1)
            i -= 1

    # собственно поиск подстроки в строке
    ind_sb = []
    k = lsb - 1  # указатель строки
    tmp = lsb - 1  # указатель строки для случая совпадения первых и последующих символов
    l = lsb - 1  # указатель образа
    while k < ls:
        if s[k] == sb[l]:
            if l == 0:
                ind_sb.append(k)
                l = lsb - 1
                k += lsb
                continue
            k -= 1
            l -= 1
        elif l != lsb - 1:  # if s[k] != sb[l]
            l = lsb - 1
            tmp += d[sb[-1]]
            k = tmp
        else:  # if s[k] != sb[l] and l == lsb - 1
            k += d[s[k]]
            tmp = k

    return ind_sb if ind_sb else None


string = input()
substring = input()
len_string, len_substring = len(string), len(substring)
print(boyer_moore_horspool(string, substring, len_string, len_substring))
