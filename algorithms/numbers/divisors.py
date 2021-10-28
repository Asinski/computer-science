def divisors(n):
    divs = set()
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        i += 1

    return sorted(divs)


n = int(input())
print(divisors(n))
