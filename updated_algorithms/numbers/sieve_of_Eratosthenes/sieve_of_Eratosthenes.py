"""
Этот метод работает за время O(n*log(log n)) и требует O(n) памяти.

Алгоритм основывается на следующем принципе: любое составное число можно представить как произведение простых чисел.
Если начать с малого числа и вычеркнуть все его кратные, то оставшиеся числа будут простыми.
"""


def sieve_of_eratosthenes(n):
    a = [True] * n
    a[0] = a[1] = False
    for k in range(2, int(n ** 0.5) + 1):  # Если число больше корня из n, то его кратные уже будут больше n.
        if a[k]:
            for m in range(2 * k, n, k):
            # for m in range(k * k, n, k):
                a[m] = False

    return a


assert sieve_of_eratosthenes(3) == [False, False, True]
assert sieve_of_eratosthenes(5) == [False, False, True, True, False]
assert sieve_of_eratosthenes(10) == [False, False, True, True, False, True, False, True, False, False]
