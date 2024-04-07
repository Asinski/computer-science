from string import ascii_lowercase as ascii


def caesar_cipher(p, k):
    ci = lambda pi, k: (ascii.index(pi) + k) % 26

    cipher_text = ''

    for pi in p:
        if pi == ' ':
            cipher_text += ' '
        else:
            cipher_text += ascii[ci(pi, k)]

    return cipher_text


if __name__ == '__main__':
    plain_text = input().lower()
    key = int(input())
    print(caesar_cipher(plain_text, key))
