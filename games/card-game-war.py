from random import shuffle


class Card:
    suits = ["пикей", "червей", "бубей", "треф"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "валета", "даму", "короля", "туза"]

    def __init__(self, value: int, suit: int):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value == other.value and self.suit < other.suit:
            return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value and self.suit > other.suit:
            return True
        return False

    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("Имя первого игрока: ")
        name2 = input("Имя второго игрока: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        while len(cards) >= 2:
            response = input("Введите X, чтобы выйти из игры. Для продолжения - любую клавишу.\n")
            if response in "XХxх":
                break
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            print(f"{self.player1.name} - {player1_card}, {self.player2.name} - {player2_card}")
            if player1_card > player2_card:
                self.player1.wins += 1
                print(f"{self.player1.name} - победитель в данному раунде!\n")
            else:
                self.player2.wins += 1
                print(f"{self.player2.name} - победитель в данному раунде!\n")
        print(f"Игра окончена. {self.winner(self.player1, self.player2)}")

    @staticmethod
    def winner(player1, player2):
        if player1.wins > player2.wins:
            return f"{player1.name} - победитель игры!"
        elif player1.wins < player2.wins:
            return f"{player2.name} - победитель игры!"
        return "Ничья!"


game = Game()
game.play_game()
