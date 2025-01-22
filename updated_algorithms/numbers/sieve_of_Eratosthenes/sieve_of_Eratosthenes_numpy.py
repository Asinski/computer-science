"""
Этот метод работает за время O(n*log(log n)) и требует O(n) памяти.

Алгоритм основывается на следующем принципе: любое составное число можно представить как произведение простых чисел.
Если начать с малого числа и вычеркнуть все его кратные, то оставшиеся числа будут простыми.
"""

import numpy as np


def sieve_of_eratosthenes_numpy(is_prime: np.ndarray) -> list[bool]:
    is_prime[:2] = False
    n_max = int(np.sqrt(len(is_prime)))  # Если число больше корня из n, то его кратные уже будут больше n.
    for i in range(2, n_max + 1):
        is_prime[2 * i::i] = False
        # is_prime[i * i::i] = False

    return list(is_prime)


assert sieve_of_eratosthenes_numpy(np.ones(3, dtype=bool)) == [np.False_, np.False_, np.True_]
assert sieve_of_eratosthenes_numpy(np.ones(5, dtype=bool)) == [np.False_, np.False_, np.True_, np.True_, np.False_]
assert sieve_of_eratosthenes_numpy(np.ones(10, dtype=bool)) == [np.False_, np.False_, np.True_, np.True_, np.False_, np.True_, np.False_, np.True_, np.False_, np.False_]
