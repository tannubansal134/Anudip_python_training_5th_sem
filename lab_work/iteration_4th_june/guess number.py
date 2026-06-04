# Guess the Secret Number Game
import random

# generate secret number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0
guess = 0

# loop until correct guess
while guess != secret_number:
    guess = int(input("Guess the number (1 to 50): "))
    attempts += 1

    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")

# display total attempts
print("Total Attempts:", attempts)