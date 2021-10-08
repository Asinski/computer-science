

def sieve_eratosthenes(n):

    a = [True] * n
    a[0] = a[1] = False
    for k in range(2, n):
        if a[k]:
            for m in range(2 * k, n, k):
                a[m] = False

    return a[2:]


n = int(input())
for i, j in enumerate(sieve_eratosthenes(n), 2):
    print(f'{i} - {"prime" if j else ""}')
