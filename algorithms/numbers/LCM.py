a, b = map(int, input().split())

pr = a * b

while b > 0:
    a, b = b, a % b

print(pr // a)
