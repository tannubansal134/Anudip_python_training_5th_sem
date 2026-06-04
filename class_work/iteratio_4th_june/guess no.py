# program to displaying the guess no
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the Number: "))

    if guess != secret_number:
        print("Wrong Guess. Try Again.")
#--------------------------------------------------------------

print("Congratulations! You guessed the correct number.")
