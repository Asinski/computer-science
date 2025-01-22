def chain_sum2(number):
    def wrapper(number2=None):
        if number2 is None:
            return wrapper.result
        wrapper.result += number2
        return wrapper

    wrapper.result = number
    return wrapper


assert chain_sum2(5)() == 5
assert chain_sum2(5)(2)() == 7
assert chain_sum2(5)(100)(-10)() == 95
