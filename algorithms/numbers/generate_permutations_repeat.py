

def generate_permutations_repeat(n: int, m: int = -1, prefix=None):
    """ Генерация всех перестановок n чисел в m позициях c повторениями """
    m = m if m != -1 else n
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep="")
        return
    for number in range(n + 1):
        prefix.append(number)
        generate_permutations_repeat(n, m - 1, prefix)
        prefix.pop()


permutations = int(input())
position = int(input())
generate_permutations_repeat(permutations, position)
