import re


def longest_word_in_file(file_name):
    the_longest_word = ''
    with open(fr'{file_name}', 'r', encoding='utf-8') as file:
        words: list = re.findall(r'\w+', file.read())
        for word in words:
            if len(word) >= len(the_longest_word):
                the_longest_word = word

    return the_longest_word