def dec_to_bin(n):
    bin_ = []
    while n > 0:
        last = n % 2
        bin_.append(last)
        n //= 2
    return ''.join(map(str, bin_[::-1]))


n = int(input())
print(dec_to_bin(n))
