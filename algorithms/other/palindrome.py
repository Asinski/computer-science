def palindrome(s):
    return s == s[::-1]


s = input()
print(palindrome(s))
