class OptimizeTailRecursion(object):
    """Оптимизация хвостовой рекурсии"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        call_result = self.func(*args, **kwargs)
        while callable(call_result):
            call_result = call_result()
        return call_result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


@OptimizeTailRecursion
def factorial(n, current_result=1):
    return current_result if n == 1 else factorial.call(n - 1, current_result * n)


n = int(input())
print(factorial(n))
