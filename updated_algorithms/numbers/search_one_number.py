from typing import List
from functools import reduce


def search1(mas: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, mas)


def search2(mas: List[int]) -> int:
    result = 0
    for num in mas:
        result ^= num
    return result


assert search1([1, 2, 1, 3, 2]) == 3
assert search2([5, 2, 1, 5, 2]) == 1
assert search1([7, 8, 3, 8, 7]) == 3
assert search2([1, 1, 2, 3, 3]) == 2
assert search1([3, 4, 3, 4, 9]) == 9
