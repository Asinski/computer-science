import random

def hangman():
    words_lists = ["тусовка", "программирование", "cекс"]
    word_num = random.randint(0,2)
    word = words_lists[word_num]
    wrong_guesses = 0
    stages = ["                 ",
              "_________        ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
              ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")

    while wrong_guesses < len(stages) - 1:
        guess = input("Введите букву: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$"
        else:
            wrong_guesses += 1
        print(" ".join(letter_board))
        print("\n".join(stages[0: wrong_guesses + 1]))
        if "_" not in letter_board:
            print("Вы выиграли! Это было слово")
            print("".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong_guesses]))
        print("Вы проиграли! Это было слово {}".format(word))

hangman()