def z_func(s):
    z = [0] * len(s)
    l = 0
    r = 0
    for i in range(1, len(z)):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while (i + z[i]) < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if (i + z[i] - 1) > r:
            l = i
            r = i + z[i] - 1

    return z


def main():
    string = input()
    substring = input()
    if not (len(string) and len(substring)):
        return None
    substr_and_str = substring + '$' + string
    result = z_func(substr_and_str)
    for i in range(len(result)):
        if result[i] == len(substring):
            print(i - len(substring) - 1, end=" ")


if __name__ == "__main__":
    main()
