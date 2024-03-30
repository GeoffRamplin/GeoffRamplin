# This program will take 2 random numbers from the user
# and the computer will select a random number.
# The user can guess the number.
import random
# Define global variables
num_1 = 0
num_2 = 0


# Number selection function
def num_selection():
    global num_1, num_2
    while True:
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
            break


# Main game function
def num_guess_game():
    random_number = random.randrange(num_1, num_2)
    num_guess = 0
    # While loop for user guesses
    while True:
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


# Start of game
print("Welcome to the number guessing game.")
print("Type 2 numbers at the prompt and begin guessing the computer's chosen number.")
print("Good luck!")

while True:
    num_selection()
    num_guess_game()
    # Option to replay the game
    replay = input("Would you like to play again? Y or N \n").lower()
    if replay == "n":
        break
    else:
        print("Lets play again!")

print("Thanks for playing!")
