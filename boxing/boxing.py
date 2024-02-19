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
        input("\nChose a boxing move: 1. Jab 2. Cross 3. Hook 4. Uppercut ")
    )
    if user_move_index not in range(1, 5):
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
        return boxing_round(fighter1, fighter2)


def boxing_fight(fighter1, fighter2, rounds, fight_details):
    fighter1_won_rounds = 0
    fighter2_won_rounds = 0
    print("Fight: " + fight_details)
    for i in range(rounds):
        round_winner = boxing_round(fighter1, fighter2)
        if round_winner == fighter1:
            fighter1_won_rounds += 1
        elif round_winner == fighter2:
            fighter2_won_rounds += 1
    if fighter1_won_rounds > fighter2_won_rounds:
        return fighter1
    return fighter2


def organize_fight():
    fighter2 = ""
    rounds = 3
    fighter1 = input("What is your name?")
    print(
        "Welcome to the boxing fight, you do you want to fight agianst a champion or a regular fighter?\n"
    )
    fight_type = int(
        input(
            "Pick:\n 1. Fight boxing champion Tyson Fury in a 5 round championship fight.\n 2. Fight in a 3 round regular fight against Anthony Joshua\n"
        )
    )
    if fight_type == 1:
        fighter2 = "Tyson Fury"
        fight_type = "Championship"
        rounds = 5
    elif fight_type == 2:
        fighter2 = "Anthony Joshua"
        fight_type = "Regular"
        rounds = 3
    else:
        if fight_type not in range(1, 2):
            print("Please chose a 1 or 2")
            organize_fight()
    winner = boxing_fight(fighter1, fighter2, rounds, "Championship")
    return winner


print("\n The winner is " + organize_fight())
