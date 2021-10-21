def generate_permutations(n: int, k: int = -1, prefix=None):
    """
    Генерация всех перестановок n чисел в k позициях (упорядоченных выборок без повторений)
    """
    k = k if k != -1 else n
    prefix = prefix or []
    if k == 0:
        print(*prefix, sep="")
        return
    for number in range(1, n + 1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, k - 1, prefix)
        prefix.pop()


permutations = int(input())
position = int(input())
generate_permutations(permutations, position)
