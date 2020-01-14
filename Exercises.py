character_name = "David"
character_age = "25"
character_sex = "Male"
print("There was a man named " + character_name)
print("He was " + character_age + " years old")
print("He also was a " + character_sex)

#Shows the letters of a certain index value
phrase = "Lip Balm"
print(phrase[2])
print(phrase[4:7])

print(phrase.index("B")) #Shows the index value

print(phrase.replace("Balm", "Moisturizer")) #Replace the values with other values

#To print, everything must be of the same text type
num = 8 * 2
print(str(num) + " is my favourite number")

print(abs(-5)) #Absolute value

print(pow(3, 2)) #Raising 3 to the power of 2

#Return the larger/smaller number
print(max(3, 7))
print(min(3,7))

print(round(4.55)) #Round the number

from math import * #Import everything (*) from math module

#Round the number to the smaller/larger
print(floor(5.99))
print(ceil(5.1))

print(sqrt(4)) #Get square root

            #Getting input from user to use the info to answer to them
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "!")
print("Your are " + age)

                        #Mad Libs Game
color = input("Enter a color")
plural_noun = input("Enter a plural noun")
celebrity = input("Enter a celebrity name")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

                            #Lists
friends = ["Kim", "Khloe", "Kourtney", "Kylie"]
print(friends[3])
print(friends[-1]) #Negative index values start from the end
print(friends[1:]) #Get everything after the second value

numbers = [2, 3, 6]

friends.extend(numbers) #merge two lists
print(friends)

friends.append("Willow") #Add an element to the list
print(friends)

#friends.clear() remove everything
#friends.pop() remove the last element

print(friends.count("Kim")) #Show the amount of time "Kim" was used in the list
print(friends)

friends.reverse() #Sort the list in reverse albhabetical or descending order
print(friends)

friends2 = friends.copy() #copy the features of friends list
print(friends2)

coordinates = (2,5) #Tuple. Unchangable, immutable. Created with (),not [] like lists

                        #Say hello to user
def say_hi(name):
    print("Hello " + name)

#A way for functions to give back information about the job rather than just doing it
def cube(num):
    return num*num*num #Without return, the result would be none, also print() can not be used inside functions
print(cube(3))

#A function that returns the max number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30, 45, 88))

                #An improved calculator
num1 = float(input("Enter first number here: "))
op = input("Enter operator here: ")
num2 = float(input("Enter second number here: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

                        #Dictionaries

Months = {
    "Feb" : "February",
    "Mar" : "March"
}
print(Months["Feb"])
print(Months.get("Feb"))
print(Months.get("Jan"))
print(Months.get("Jan", "Not a valid key" ))

                        #While loop
i = 1
while i <= 10:
    print(i)
    i += 1
    print("Done with loop")

                        #Guessing game
secret_word = "berk"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. You lose!")
else:
    print("You win!")

                            #For loop
for friend in friends2:
    print(friend)

for index in range(10): #from 0 to 9
    print(index)

for index in range(3, 10): #from 3 to 9
    print(index)

for index in range(len(friends)):
    print(friends[index])
for index in friends: #The same thing with above
    print(index)

                        #Exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

                            #2D Lists
number_grid = [
    [1, 2, 3],
    [3, 4, 5],
    [7, 8, 9],
    [0]
]
print(number_grid[0][1]) #1st column, 2nd row

for row in number_grid:
    print(row) #Show the grid as it is

for row in number_grid:
    for col in row:
        print(col) #Show every element of the grid one by one

#Translator: Change vowels into the letter B
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "B"
            else:
                translation = translation + "b"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase :")))

                            #Try, except

try:
    number = int(input("Enter a number: ")) #Possible error: ValueError
    print(number)
except:
    print("Invalid Input")

try:
    value = 10/0
    number = int(input("Enter a number: ")) #Possible error: ValueError
    print(number)
except ZeroDivisionError as err: #Make the error a variable, can print the variable instead of error text
    print("Division by zero")
except ValueError:
    print("Invalid input")

                            #Reading Files

employee_file = open("employees", "r") #r=read w=write a=append
#Input directory if two sheets are not in the same folder
#If not exist, it will create a new file with this name

print(employee_file.read()) #Show the whole sheet

print(employee_file.readline()) #Show the current line, pass to the next one
print(employee_file.readline()) #Show the next line and so on

#print(employee_file.readlines()[0]) Show 1st  but python won't read the same line twice
print(employee_file.readlines()) #Show each line in an array

print(employee_file.readable()) #True if the "r" has been input

for employee in employee_file.readlines():
    print(employee) #Show each line

employee_file.close() #Don't forget to close

                            #Writing Files

#employee_file_a = open("employees", "a")

#employee_file_a.write("Toby - Human Ressources") #If you run this again, you will write another in the same line
#employee_file_a.write("\nKelly - Customer Service") #Write at the end of the file, in a new line

#employee_file_a.close()

#employee_file_w = open("employees", "w")

#employee_file.write("\nKelly - Customer Service") Will replace the whole sheet with this line

                            #Modules
#import useful_tools - imports every function from the sheet useful_tools
#useful_tools.example(10)

                        #Class & Objects
#Class is a custom data type

class Student:
    def __init__(self, name, major, gpa, in_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.in_probation = in_probation

    def on_honor_roll(self): #Example of a function inside a class
        if self.gpa >= 3.5:
            return True
        else:
            return False

student1 = Student("Jim", "Business", 3.1, False) #This is an object. An instance of the datatype

print(student1.name)
print(student1.major)

print(student1.on_honor_roll()) #A boolean. Used as an object method.

                            #Building a quiz

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
]

from Question import Question
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questions) :
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("You've got " + str(score) + "/" + str(len(questions)) + "correct!")

run_test(questions)

                                #Inheritence
#Inheriting a class' attributes to another one without writing them from scratch

from Chef import Chef
from ChineseChef import ChineseChef
myChef = Chef()
myChef.make_special_dish() #Chef's special dish is BBQ
#Chef.make_salad() won't work. Needs to be a variable first

myChineseChef = ChineseChef() #Brackets are important
myChineseChef.make_salad()
myChineseChef.make_special_dish()

                            #Interpreter
#You can use your OS command prompt as a python interpreter. By entering python3 in your cmd
#you will access the interpreter. In windows you might get problems, you have to google how to
#make windows recognize this command
