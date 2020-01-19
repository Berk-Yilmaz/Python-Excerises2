secret_word = "forest"
game = True
while game == True:
    guess = input("Enter your guess: ")

    if guess in secret_word:
        print("Correct! There is one " + str(guess) + " in there!")

    else:
        print("Sorry. There is no " + str(guess) + " in there.")

    for guess in secret_word:
        print(guess)