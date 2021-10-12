

def generate_permutations(n: int, m: int = -1, prefix=None):
    """ Генерация всех перестановок n чисел в m позициях """
    m = m if m != -1 else n
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep="")
        return
    for number in range(n):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()


permutations = int(input())
position = int(input())
generate_permutations(permutations, position)
