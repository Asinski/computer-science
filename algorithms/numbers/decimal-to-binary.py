n = int(input())

b = []

while n > 0:
    last = n % 2
    b.append(last)
    n //= 2

print("".join(map(str, b[::-1])))