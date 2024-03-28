# This program will take 2 random numbers from the user
# and the computer will select a random number.
# The user can guess the number.

import random

condition = True
print("Welcome to the number guessing game.")
print("Type 2 numbers at the prompt and begin guessing the computer's chosen number.")
print("Good luck!")
# While loop for main game
while condition:
    print("Type a range of numbers and guess a randomly selected number.")
    try:
        num_1 = int(input("Enter your first number: "))
    except ValueError:
        print("You must enter a number!")
        continue
    try:
        num_2 = int(input("Enter your second number: "))
    except ValueError:
        print("You must enter a number!")
        continue
    if num_1 == num_2:
        print("You must select a different number")
        try:
            num_2 = int(input("Enter your second number: "))
        except ValueError:
            print("You must enter a number!")
            continue
    else:
        continue
    random_number = random.randrange(num_1, num_2)
    num_guess = 0
    # While loop for user guesses
    while condition:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("You must enter a number!")
            continue
        if guess == random_number:
            print(f"Well done, you guessed correctly and it took you {num_guess} times!\n")
            break
        elif guess < random_number:
            print("That is incorrect, your guess was too low.")
            num_guess += 1
        elif guess > random_number:
            print("That is incorrect, your guess was too high.")
            num_guess += 1
    # Option to replay the game
    replay = input("Would you like to play again? Y or N \n").lower()
    if replay == "n":
        condition = False
    else:
        print("Lets play again!")

print("Thanks for playing!")
