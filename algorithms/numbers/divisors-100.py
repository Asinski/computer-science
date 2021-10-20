n = int(input())

i = 1
a = []

while i ** 2 <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)

    i += 1

print(*sorted(a))
