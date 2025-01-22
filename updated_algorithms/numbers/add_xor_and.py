def add(a: int, b: int) -> int:
    while b != 0:
        carry = a & b  # Вычисляем перенос.
        a = a ^ b  # Складываем без переноса.
        b = carry << 1  # Перенос смещаем на один бит влево.
    return a


assert add(3, 2) == 5
assert add(5, 0) == 5
assert add(0, 5) == 5
assert add(0, 0) == 0
