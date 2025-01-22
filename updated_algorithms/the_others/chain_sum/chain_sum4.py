def chain_sum4(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper

        logic = {
            type(None): lambda: wrapper.result,  # type(None) -> NoneType
            int: inner
        }
        return logic[type(number2)]()

    wrapper.result = number
    return wrapper


assert chain_sum4(5)() == 5
assert chain_sum4(5)(2)() == 7
assert chain_sum4(5)(100)(-10)() == 95
