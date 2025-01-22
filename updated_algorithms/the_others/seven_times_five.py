def _digit(number, operator=None):
    if operator is None:
        return number
    return operator(number)

def zero(operator=None): return _digit(0, operator)
def one(operator=None): return _digit(1, operator)
def two(operator=None): return _digit(2, operator)
def three(operator=None): return _digit(3, operator)
def four(operator=None): return _digit(4, operator)
def five(operator=None): return _digit(5, operator)
def six(operator=None): return _digit(6, operator)
def seven(operator=None): return _digit(7, operator)
def eight(operator=None): return _digit(8, operator)
def nine(operator=None): return _digit(9, operator)

def plus(second_operand): return lambda first_operand: first_operand + second_operand
def minus(second_operand): return lambda first_operand: first_operand - second_operand
def times(second_operand): return lambda first_operand: first_operand * second_operand
def divided_by(second_operand): return lambda first_operand: first_operand / second_operand


assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3.0
