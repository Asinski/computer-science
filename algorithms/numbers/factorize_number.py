def factorize_number(n):
    if n == 0:
        return None

    multipliers = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            multipliers.append(divisor)
            n /= divisor
        else:
            divisor += 1

    return multipliers


n = int(input())
print(*factorize_number(n))
