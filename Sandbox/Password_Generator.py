import random
import getpass

Characters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
              "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
              "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

def generate(lenght):
    password = ""
    login = False

    for len in range(lenght):
       password += Characters[random.randrange(0, 51)]
    print("Your password is: " + password)
    while login == False:
        validation = input("Enter your password: ")
        if validation == password:
            print("You have successfully logged in.")
            login = True
        else:
            print("Incorrect password.")