def knut_morris_pratt(s, sb):
    """
    Алгоритм Кнута-Морриса-Пратта (Матиясевича) поиска подстроки в строке. Сложность - O(N + M).
    Возвращает индекс(ы) строки, с которого(ых) начинается подстрока.
    """
    if not (len(s) and len(sb)):
        return None

    # реализация пи-функции и формирование пи-массива, используемого при сдвиге образа вдоль строки
    pi = [0 for _ in range(len(sb))]
    i = 1
    j = 0
    while i < len(sb):
        if sb[i] == sb[j]:
            pi[i] = j + 1
            i += 1
            j += 1
        elif j == 0:  # if sb[i] != sb[j]
            pi[i] = 0
            i += 1
        else:  # if sb[i] != sb[j] and j != 0
            j = pi[j - 1]

    # собственно поиск подстроки в строке
    ind_sb = []
    k = 0  # указатель строки
    l = 0  # указатель образа
    while k < len(s):
        if s[k] == sb[l]:
            if l == len(sb) - 1:
                ind_sb.append(k - l)
                k += 1
                l = 0
                continue
            k += 1
            l += 1
        elif l == 0:  # if s[k] != sb[l]
            if k == len(s) - 1:
                return None
            k += 1
        else:  # if s[k] != sb[l] and l != 0
            l = pi[l - 1]

    return ind_sb if ind_sb else None


string = input()
substring = input()
print(knut_morris_pratt(string, substring))
