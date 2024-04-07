def check_prime(n):
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor ** 2 <= n and n % divisor != 0:
        divisor += 2

    return divisor ** 2 > n


n = int(input())
print(check_prime(n))
