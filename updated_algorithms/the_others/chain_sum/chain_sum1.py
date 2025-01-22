def chain_sum1(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper

    return wrapper


assert chain_sum1(5)() == 5
assert chain_sum1(5)(2)() == 7
assert chain_sum1(5)(100)(-10)() == 95
