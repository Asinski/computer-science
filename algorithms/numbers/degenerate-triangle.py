def degenerate_triangle(a, b, c):
    return "YES" if a < (b + c) and b < (a + c) and c < (a + b) else "NO"


def main():
    troom, tcond = map(int, input().split())
    mode = input()
    print(conditioner(troom, tcond, mode))


if __name__ == '__main__':
    main()