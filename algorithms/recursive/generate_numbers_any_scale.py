def generate_numbers(n, m, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep="")  # print("".join(map(str, prefix)))
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


scale, length_number = map(int, input().split())
generate_numbers(scale, length_number)
