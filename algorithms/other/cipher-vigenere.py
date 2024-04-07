from string import ascii_lowercase as ascii


def vigenere_cipher(p, k):
    ci = lambda pj, kj: (ascii.index(pj) + ascii.index(kj)) % 26

    cipher_text_key = ''
    cipher_text = ''

    i = 0
    for pi in p:
        if pi == ' ':
            cipher_text_key += ' '
        else:
            cipher_text_key += k[i % len(k)]
            i += 1

    for j in range(len(cipher_text_key)):
        if cipher_text_key[j] == ' ':
            cipher_text += ' '
        else:
            cipher_text += ascii[ci(p[j], cipher_text_key[j])]

    return cipher_text


if __name__ == '__main__':
    plain_text = input().lower()
    key = input()
    print(vigenere_cipher(plain_text, key))
