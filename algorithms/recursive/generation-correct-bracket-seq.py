def bracket(count, s='', left=0, right=0):
    if left == right == count:
        print(s)
    else:
        if left < count:
            bracket(count, s + '(', left + 1, right)
        if right < left:
            bracket(count, s + ')', left, right + 1)


def main():
    n = int(input())
    bracket(n)


if __name__ == "__main__":
    main()
