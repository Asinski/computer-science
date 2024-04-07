def equal_str(a: str, b: str):
    # if len(a) != len(b):
    #     return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def search_substr(s, sb):
    """
    Прямой поиск, или наивный алгоритм поиска подстроки в строке. Сложность - O(NM).
    Возвращает индекс(ы) строки, с которого(ых) начинается подстрока.
    """
    ind_sb = []
    for i in range(len(s) - len(sb) + 1):
        if equal_str(s[i:i + len(sb)], sb):
            ind_sb.append(i)

    return ind_sb if ind_sb else None


string = input()
substring = input()
print(*search_substr(string, substring))
