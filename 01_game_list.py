import random

how_many = 5
won = 0
lost = 0

game_history = []

print()
print("***** world's lamest game *****")
print("type in 'won' to win, or anything else to lose a round")
print()

for item in range(1,how_many + 1):

    result = input("game result? ")

    if result == "won":
        feedback = "you won"
        won += 1
    else:
        feedback = "sorry, you lost"
        lost += 1

    rounds_results = "round {}: {}".format(item, feedback)
    game_history.append(rounds_results)

print()
print("***** results *****")

for item in game_history:
    print(item)