dictionary = {}

while True:
    word = input().lower()
    if word in dictionary:
        print(f"Слово {word} переводится как {dictionary[word]}")
    else:
        print(f"Введите перевод слова {word}")
        dictionary[word] = input().lower()
