def hanoi(n, i, k):
    if n == 1:
        print('Диск 1 со штыря {0} на штырь {1}'.format(i, k))
        return
    tmp = 6 - i - k
    hanoi(n - 1, i, tmp)
    print('Диск {0} со штыря {1} на штырь {2}'.format(n, i, k))
    hanoi(n - 1, tmp, k)


count_disk, pin1, pin2 = map(int, input().split())
hanoi(count_disk, pin1, pin2)
