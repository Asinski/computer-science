class OptimizeTailRecursion(object):

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
def factorial_while_decorator_tco2(n, current_result=1):
    return current_result if n == 1 else factorial_while_decorator_tco2.call(n - 1, current_result * n)


assert factorial_while_decorator_tco2(2) == 2
assert factorial_while_decorator_tco2(3) == 6
assert factorial_while_decorator_tco2(4) == 24
