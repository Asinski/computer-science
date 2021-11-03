from typing import List
from functools import reduce


def search(a: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, a)


assert search([1, 2, 1, 3, 2]) == 3
assert search([5, 2, 1, 5, 2]) == 1
assert search([7, 8, 3, 8, 7]) == 3
assert search([1, 1, 2, 3, 3]) == 2
assert search([3, 4, 3, 4, 9]) == 9


massive = list(map(int, input().split()))
search(massive)
