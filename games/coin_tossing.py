from random import choice

coin = ["Орёл", "Решка"]
toss = choice(coin)

selection = input("Орёл или Решка?\n").capitalize()

if selection == toss:
    print(f"You win! The coin landed on {toss}")
else:
    print(f"You lose! The coin landed on {toss}")
