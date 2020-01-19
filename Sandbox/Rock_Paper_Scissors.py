import random

def rps_game():
    signs = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0

    us = str(user_score)
    cs = str(computer_score)

    while computer_score < 3 and user_score < 3:

        choice = signs[random.randrange(0, 3)]
        answer = input("Rock, Paper, Scissors?\n")

        if answer in ("Rock", "Paper", "Scissors"):
            print("Opponent shows: " + choice + "!")
            if answer == choice:
                print("Draw! " + us + " - " + cs)
            elif answer == "Rock":
                if choice == "Paper":
                    computer_score += 1
                    print("You lose! " + us + " - " + cs)
                elif choice == "Scissors":
                    user_score += 1
                    print("You win! " + us + " - " + cs)
            elif answer == "Paper":
                if choice == "Rock":
                    user_score += 1
                    print("You win! " + us + " - " + cs)
                elif choice == "Scissors":
                    computer_score += 1
                    print("You lose! " + us + " - " + cs)
            elif answer == "Scissors":
                if choice == "Rock":
                    computer_score += 1
                    print("You lose! " + str(user_score) + " - " + str(computer_score))
                elif choice == "Paper":
                    user_score += 1
                    print("You win! " + str(user_score) + " - " + str(computer_score))
            print(str(user_score) + "-" + str(computer_score))
        else:
            print("Invalid answer")

    print("Game over!")
rps_game()