def generate_permutations_repeat(n: int, k: int = -1, prefix=None):
    """
    Генерация всех слов (упорядоченных выборок с повторениями)
    """
    k = k if k != -1 else n
    prefix = prefix or []
    if k == 0:
        print(*prefix, sep="")
        return
    for number in range(1, n + 1):
        prefix.append(number)
        generate_permutations_repeat(n, k - 1, prefix)
        prefix.pop()


permutations = int(input())
position = int(input())
generate_permutations_repeat(permutations, position)
