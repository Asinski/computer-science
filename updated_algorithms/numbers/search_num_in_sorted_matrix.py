from typing import Optional, Union

# O(M + N)

def search_in_matrix(matrix: list[list[int]], target: int) -> Optional[Union[tuple[int, int], False]]:
    if not matrix:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Начинаем с правого верхнего угла.

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row, col  # Нашли элемент.
        elif matrix[row][col] > target:
            col -= 1  # Идем влево.
        else:
            row += 1  # идем вниз

    return None  # Элемент не найден.


matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
assert search_in_matrix(matrix, 9) == (2, 2)
assert search_in_matrix(matrix, 10) == (3, 0)
assert search_in_matrix(matrix, 1) == (0, 0)
assert search_in_matrix(matrix, 17) == (3, 3)
assert search_in_matrix(matrix, 0) is None
assert search_in_matrix([], 20) is False
