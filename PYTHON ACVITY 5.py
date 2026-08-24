# Activity 5: Guessing game

import random

# Generate a random number between 1 and 20
number = random.randint(1, 20)

# Give the user 5 attempts
attempts = 5

print("WELCOME ALL TO THE GUESSING GAME")
print("Guess a number between 1 and 20.")
print("You have 5 attempts.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(" Congratulations You guessed the correct number!!!")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    attempts -= 1
    print("Attempts remaining:", attempts)

if attempts == 0:
    print("X YOU LOST THE RIGHT NUMBER WAS ", number)
