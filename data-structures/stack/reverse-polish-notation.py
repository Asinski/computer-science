"""
Постфиксная (или обратная польская) запись арифметического выражения — это способ записи выражений,
в котором знак операции записывается не между операндами, а после операндов.
"""
from stack import Stack


def calculate(nt: str) -> int:
    polish_stack = Stack()
    for item in range(len(nt)):
        if nt[item] in "+-*//":
            y = polish_stack.pop()
            x = polish_stack.pop()
            if nt[item] == "+":
                polish_stack.push(y + x)
            elif nt[item] == "-":
                polish_stack.push(y - x)
            elif nt[item] == "*":
                polish_stack.push(y * x)
            else:
                polish_stack.push(y // x)
        else:
            polish_stack.push(int(nt[item]))

    return polish_stack.peek()


nt = input()
print(calculate(nt))
