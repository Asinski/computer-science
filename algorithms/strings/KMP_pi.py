def pi_func(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while s[i] != s[j] and j > 0:
            j = pi[j - 1]
        if s[i] == s[j]:
            pi[i] = j + 1
        else:
            pi[i] = 0

    return pi


def main():
    string = input()
    substring = input()
    if not (len(string) and len(substring)):
        return None
    substr_and_str = substring + '$' + string
    result = pi_func(substr_and_str)
    for i in range(len(result)):
        if result[i] == len(substring):
            print(i - 2 * len(substring), end=" ")


if __name__ == "__main__":
    main()
