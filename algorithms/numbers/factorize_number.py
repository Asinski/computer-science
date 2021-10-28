def factorize_number(n):
    if n <= 0:
        return None

    tmp = n

    multipliers = []
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            multipliers.append(divisor)
            n //= divisor
        else:
            divisor += 1

    if n != 1 and n != tmp:
        multipliers.append(n)
    else:
        return f'a prime number'

    return multipliers


n = int(input())
print(factorize_number(n))
