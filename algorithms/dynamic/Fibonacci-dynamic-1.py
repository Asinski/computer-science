def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n, fib):
    result = None
    try:
        for i in range(n):
            result = next(fib)
    except StopIteration:
        pass
    return result


n = int(input())
print(take(n, fibonacci()))
