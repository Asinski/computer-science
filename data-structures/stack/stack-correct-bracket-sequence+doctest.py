from stack import Stack
import doctest


def check(s: str):
    """
    Проверка скобочной последовательности на корректность.
    Use case следующий:
    >>> check("")
    True
    >>> check("()")
    True
    >>> check("(())")
    True
    >>> check("()()()()")
    True
    >>> check("((({[]}))){[]}")
    True
    >>> check("(()))")
    False
    >>> check("})})")
    False
    >>> check("((())")
    False
    >>> check("([)]")
    False
    >>> check("((((((")
    False
    >>> check(")")
    False
    """
    bracket_stack = Stack()
    for i in s:
        if i in "({[":
            bracket_stack.push(i)
        elif i in ")}]":
            if bracket_stack.isempty():
                return False
            open_bracket = bracket_stack.pop()
            if open_bracket == "(" and i == ")":
                continue
            if open_bracket == "{" and i == "}":
                continue
            if open_bracket == "[" and i == "]":
                continue
            return False

    return bracket_stack.isempty()


def main():
    bracket_string = input()
    print(check(bracket_string))


if __name__ == "__main__":
    doctest.testmod(verbose=False)
    main()
