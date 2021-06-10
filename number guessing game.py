import random

number = random.randrange(1 , 50)
guess = int(input("Guess the number between 1 to 50 : "))

while guess != number:

    if guess < number:
        print("You need to guess higher. Try again.")
        guess = int(input("\n guess the no. betwween 1 to 50 : "))

    if guess > number:
        print("You need to guess lower. Try again.")
        guess = int(input("\n guess the no. betwween 1 to 50 : "))


print("CONGRATULATION ! You sucessfully geussed the number ")
