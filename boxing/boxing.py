import random

boxing_moves = {
    "Jab": ["Hook", "Cross"],
    "Cross": ["Jab", "Uppercut"],
    "Hook": ["Uppercut", "Jab"],
    "Uppercut": ["Cross", "Hook"],
}


def boxing_round(fighter1, fighter2):
    moves = list(boxing_moves)
    user_move_index = int(
        input("Chose a boxing move: 1. Jab 2. Cross 3. Hook 4. Uppercut ")
    )
    if user_move_index not in range(1, 4):
        print("Please chose a number between 1-4")
        boxing_round(fighter1, fighter2)

    random_move_index = random.randint(1, 4)
    user_move = list(boxing_moves.keys())[user_move_index - 1]
    random_moves = boxing_moves.get(moves[random_move_index - 1])
    if user_move in random_moves:
        index = random_moves.index(user_move)
        if index == 0:
            print("You lost the round")
            return fighter1
        else:
            print("You won the round")
            return fighter2
    else:
        print("\nRound still not done\n")
        boxing_round(fighter1, fighter2)
    return


def boxing_fight():

    return


def organize_fight():

    return


boxing_round("", "")
