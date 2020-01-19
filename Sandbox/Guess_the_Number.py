import random

def game():

    random.seed()
    secret_number = int(random.randrange(0, 10))
    answer = ""
    guess_count = 0
    remaining_guesses = 3

    while answer != secret_number and remaining_guesses > 0:
        answer = int(input("Enter your guess: "))
        guess_count += 1
        remaining_guesses -= 1
        print(str(remaining_guesses) + " Guesses remaining.")

        if answer < secret_number:
            print("Too low!")
        elif answer > secret_number:
            print("Too high!")

    if remaining_guesses <= 0:
        print("You lost. Out of guesses!")
        print(secret_number)
    elif answer == secret_number:
        print("You've won!")


game()