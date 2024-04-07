from string import punctuation


def longest_word_in_file(file_name):
    the_longest_word = ''
    with open(fr'{file_name}', 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                word_without_mark = remove_punctuation(word)
                if len(word_without_mark) >= len(the_longest_word):
                    the_longest_word = word_without_mark

    return the_longest_word


def remove_punctuation(word):
    for mark in punctuation:
        if mark in word:
            word = word.replace(mark, '')

    return word
