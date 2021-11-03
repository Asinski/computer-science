def radix_sort(massive_need_sort: list) -> list:
    """
    Radix sort is a non-comparative sorting algorithm.
    It avoids comparison by creating and distributing elements into buckets according to their radix.

    Применение поразрядной сортировки имеет одно ограничение: перед началом сортировки необходимо знать
        length – максимальное количество разрядов в сортируемых величинах
                 (например, при сортировке слов необходимо знать максимальное количество букв в слове),
        rang – количество возможных значений одного разряда (при сортировке слов – количество букв в алфавите).
    Для сортировки чисел второе число заранее известно: количество цифр равно основанию системы счисления.

    Сложность алгоритма: O(NK) по времени и O(K) по памяти.
    """
    length = len(str(max(massive_need_sort)))
    rang = 10
    for degree in range(length):
        rang_massive = [[] for _ in range(rang)]
        for number in massive_need_sort:
            figure = (number // (10 ** degree)) % 10  # number // 10 ** degree % 10
            rang_massive[figure].append(number)
        massive_need_sort[:] = []
        for sub_rang_massive in range(rang):
            massive_need_sort = massive_need_sort + rang_massive[sub_rang_massive]

    return massive_need_sort


massive = list(map(int, input().split()))
print(radix_sort(massive))
