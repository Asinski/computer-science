def chain_sum3(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        try:
            number2 = int(number2)
        except TypeError:
            return result
        result += number2
        return wrapper

    return wrapper


assert chain_sum3(5)() == 5
assert chain_sum3(5)(2)() == 7
assert chain_sum3(5)(100)(-10)() == 95
